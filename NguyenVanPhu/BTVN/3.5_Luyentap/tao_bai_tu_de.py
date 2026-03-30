import argparse
import re
import subprocess
import sys
import unicodedata
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


def bo_dau(text):
    text = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in text if unicodedata.category(ch) != "Mn")


def doc_de_bai(input_file):
    if input_file:
        return Path(input_file).read_text(encoding="utf-8")

    print("Dán đề bài vào đây rồi nhấn Ctrl+D:")
    return sys.stdin.read()


def tim_so_bai(text):
    text_khong_dau = bo_dau(text).lower()
    matches = re.findall(r"\bbai\s*(\d+)\b", text_khong_dau)

    so_bai = []
    for item in matches:
        number = int(item)
        if number not in so_bai:
            so_bai.append(number)

    return so_bai


def lay_mau_code(so_bai):
    source_file = SCRIPT_DIR / f"bai{so_bai}.py"
    if source_file.exists():
        return source_file.read_text(encoding="utf-8")
    return None


def tao_file_bai(ds_bai, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    da_tao = []
    chua_ho_tro = []

    for so_bai in ds_bai:
        code = lay_mau_code(so_bai)
        if code is None:
            chua_ho_tro.append(so_bai)
            continue

        output_file = output_dir / f"Bai{so_bai}.py"
        output_file.write_text(code, encoding="utf-8")
        da_tao.append(output_file)

    return da_tao, chua_ho_tro


def chay_lenh_git(repo_root, args):
    subprocess.run(["git", "-C", str(repo_root), *args], check=True)


def tim_git_root(output_dir):
    result = subprocess.run(
        ["git", "-C", str(output_dir), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        return None

    return Path(result.stdout.strip())


def day_len_github(output_dir, files, message):
    repo_root = tim_git_root(output_dir)
    if repo_root is None:
        print("Không tìm thấy repo git, bỏ qua bước push.")
        return

    relative_files = [str(path.resolve().relative_to(repo_root)) for path in files]

    try:
        chay_lenh_git(repo_root, ["add", *relative_files])

        result = subprocess.run(
            ["git", "-C", str(repo_root), "diff", "--cached", "--quiet", "--", *relative_files],
            check=False,
        )
        if result.returncode == 0:
            print("Không có thay đổi mới để commit.")
            return

        chay_lenh_git(repo_root, ["commit", "-m", message])
        chay_lenh_git(repo_root, ["push", "origin", "HEAD"])
    except subprocess.CalledProcessError:
        print("Push lên GitHub không thành công. Hãy kiểm tra tài khoản git hoặc quyền truy cập repo.")


def main():
    parser = argparse.ArgumentParser(
        description="Tự động tạo file Python từ đề bài và có thể đẩy code lên GitHub."
    )
    parser.add_argument(
        "--input",
        help="Đường dẫn tới file chứa đề bài. Nếu bỏ trống thì nhập từ bàn phím.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(SCRIPT_DIR),
        help="Thư mục chứa các file BaiX.py được tạo ra.",
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Tự động git add, commit và push các file vừa tạo.",
    )
    parser.add_argument(
        "--message",
        default="Tự động tạo bài tập Python từ đề bài",
        help="Nội dung commit khi dùng --push.",
    )
    args = parser.parse_args()

    de_bai = doc_de_bai(args.input)
    ds_bai = tim_so_bai(de_bai)

    if not ds_bai:
        print("Không tìm thấy số bài trong đề.")
        return

    da_tao, chua_ho_tro = tao_file_bai(ds_bai, args.output_dir)

    if da_tao:
        print("Đã tạo các file:")
        for path in da_tao:
            print("-", path.name)
    else:
        print("Không tạo được file nào.")

    if chua_ho_tro:
        print("Các bài chưa có mẫu code:", ", ".join(str(x) for x in chua_ho_tro))

    if args.push and da_tao:
        day_len_github(args.output_dir, da_tao, args.message)
        print("Đã đẩy code lên GitHub.")


if __name__ == "__main__":
    main()
