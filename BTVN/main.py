import os
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

try:
    from google import genai
    from google.genai.errors import APIError, ClientError, ServerError
except ImportError:
    genai = None
    APIError = Exception
    ClientError = Exception
    ServerError = Exception


# Dùng model Gemini đơn giản, nhanh và phù hợp cho bài tập cơ bản.
MODEL_NAME = "gemini-2.5-flash"


def tao_prompt(yeu_cau):
    """Tạo prompt yêu cầu AI chỉ trả về code Python đơn giản."""
    return (
        "Bạn là trợ lý sinh code Python cho sinh viên mới học.\n"
        "Chỉ trả về code Python.\n"
        "Không giải thích dài dòng.\n"
        "Không dùng markdown.\n"
        "Không dùng ```.\n"
        "Code phải ngắn gọn, dễ hiểu.\n"
        "Nếu cần nhập dữ liệu thì dùng input().\n"
        "Ưu tiên cách viết cơ bản, không dùng kỹ thuật nâng cao.\n"
        "Yêu cầu bài lập trình:\n"
        f"{yeu_cau}"
    )


def lam_sach_code(noi_dung):
    """Xóa dấu ``` nếu AI lỡ trả về markdown."""
    noi_dung = noi_dung.strip()

    if not noi_dung.startswith("```"):
        return noi_dung

    cac_dong = noi_dung.splitlines()

    if cac_dong:
        cac_dong = cac_dong[1:]

    if cac_dong and cac_dong[-1].strip() == "```":
        cac_dong = cac_dong[:-1]

    return "\n".join(cac_dong).strip()


def xoa_noi_dung():
    """Xóa ô nhập và ô kết quả."""
    o_nhap.delete("1.0", tk.END)
    o_ket_qua.delete("1.0", tk.END)
    o_nhap.focus()


def sinh_code():
    """Gửi yêu cầu lên Gemini API và hiển thị code trả về."""
    yeu_cau = o_nhap.get("1.0", tk.END).strip()

    if not yeu_cau:
        messagebox.showwarning("Thiếu dữ liệu", "Bạn chưa nhập yêu cầu bài lập trình.")
        return

    if genai is None:
        messagebox.showerror(
            "Thiếu thư viện",
            "Chưa cài thư viện google-genai.\nHãy chạy lệnh: pip install google-genai",
        )
        return

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        messagebox.showerror(
            "Thiếu API key",
            "Chưa tìm thấy GEMINI_API_KEY.\n"
            'Hãy mở terminal và chạy: export GEMINI_API_KEY="api_key_cua_ban"',
        )
        return

    o_ket_qua.delete("1.0", tk.END)
    o_ket_qua.insert(tk.END, "Đang sinh code, vui lòng chờ...\n")
    cua_so.update_idletasks()

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=tao_prompt(yeu_cau),
        )

        code = lam_sach_code((response.text or "").strip())

        o_ket_qua.delete("1.0", tk.END)
        if code:
            o_ket_qua.insert(tk.END, code)
        else:
            o_ket_qua.insert(tk.END, "# Không nhận được code từ AI.")

    except ClientError as loi:
        o_ket_qua.delete("1.0", tk.END)
        messagebox.showerror(
            "Lỗi yêu cầu",
            f"Không gọi được Gemini API.\nMã lỗi: {getattr(loi, 'status', 'N/A')}\n"
            f"Chi tiết: {getattr(loi, 'message', str(loi))}",
        )
    except ServerError as loi:
        o_ket_qua.delete("1.0", tk.END)
        messagebox.showerror(
            "Lỗi máy chủ",
            "Máy chủ Gemini đang bận hoặc tạm thời lỗi.\n"
            f"Chi tiết: {getattr(loi, 'message', str(loi))}",
        )
    except APIError as loi:
        o_ket_qua.delete("1.0", tk.END)
        messagebox.showerror(
            "Lỗi API",
            f"Mã lỗi: {getattr(loi, 'status', 'N/A')}\n"
            f"Chi tiết: {getattr(loi, 'message', str(loi))}",
        )
    except Exception as loi:
        o_ket_qua.delete("1.0", tk.END)
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {loi}")


# Tạo cửa sổ chính.
cua_so = tk.Tk()
cua_so.title("Sinh code Python bằng Gemini")
cua_so.geometry("840x620")


tk.Label(
    cua_so,
    text="Nhập yêu cầu bài lập trình Python",
    font=("Arial", 14, "bold"),
).pack(pady=10)

tk.Label(
    cua_so,
    text='Ví dụ: "Viết chương trình tính tổng từ 1 đến n"',
    font=("Arial", 10),
).pack(pady=(0, 8))


# Ô nhập yêu cầu.
o_nhap = ScrolledText(cua_so, height=6, font=("Arial", 11))
o_nhap.pack(fill="x", padx=12)


# Khung chứa nút bấm.
khung_nut = tk.Frame(cua_so)
khung_nut.pack(pady=10)

tk.Button(khung_nut, text="Sinh code", width=14, command=sinh_code).pack(
    side="left", padx=8
)
tk.Button(khung_nut, text="Xóa", width=14, command=xoa_noi_dung).pack(
    side="left", padx=8
)


tk.Label(
    cua_so,
    text="Code Python kết quả",
    font=("Arial", 12, "bold"),
).pack(pady=(10, 5))


# Ô hiển thị kết quả.
o_ket_qua = ScrolledText(cua_so, font=("Consolas", 11))
o_ket_qua.pack(fill="both", expand=True, padx=12, pady=(0, 12))

o_nhap.focus()


# Chạy giao diện.
cua_so.mainloop()
