import difflib
import black
import autopep8

# 整形前のコード(コードをそのまま記載)
code_before = """

"""

# 整形後のコード（Blackで整形）
code_after_black = black.format_str(code_before, mode=black.FileMode())

# 整形後のコード（autopep8で整形）
code_after_autopep8 = autopep8.fix_code(code_before)

# 差分を比較する関数
def show_diff(before, after):
    diff = difflib.unified_diff(before.splitlines(), after.splitlines(), lineterm='', fromfile='Before', tofile='After')
    return '\n'.join(diff)

# 差分を表示
print("== Diff using Black ==\n")
print(show_diff(code_before, code_after_black))

print("\n== Diff using autopep8 ==\n")
print(show_diff(code_before, code_after_autopep8))
