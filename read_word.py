import docx
import save_data
import os

path = '.\data_all'
save_path = '.\save_data'
files = os.listdir(path)

if not os.path.exists(save_path):
    os.makedirs(save_path)

save_data.delete(save_path)

for file in files:
    if not os.path.isdir(file):
        doc = docx.Document(path + '/' + file)
        for para in doc.paragraphs:
            data = para.text
            if len(data) > 20:
                r1, r2, r3 = save_data.match(data)
                file_new = file.replace('.docx', '.csv')
                save_data.save(r1, r2, r3, save_path + '/' + file_new)
