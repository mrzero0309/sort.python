def copy_next_n_lines(input_path, output_path, start_line, n_lines):
    with open(input_path, 'r',encoding='utf-8') as input_file:
        lines = input_file.readlines()

    # Ghi n dòng tiếp theo vào tệp mới
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(lines[start_line:start_line + n_lines])

# Thay đổi đường dẫn tới tệp đầu vào và tệp đầu ra của bạn
input_file_path = 'input2.txt'
output_file_path = 'out.txt'
start_line = 10  # Dòng bắt đầu
number_of_lines_to_copy = 20  # Số dòng bạn muốn sao chép

copy_next_n_lines(input_file_path, output_file_path, start_line, number_of_lines_to_copy)