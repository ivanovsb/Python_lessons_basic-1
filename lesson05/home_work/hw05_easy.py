# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
for i in range(1,10):
dir_name = 'dir_{0}'.format(str(i))
os.mkdir(dir_name)

for i in range(1,10):
dir_name = 'dir_{0}'.format(str(i))
os.rmdir(dir_name)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os
thedir = os.getcwd()
d = [name for name in os.listdir(thedir) if os.path.isdir(os.path.join(thedir, name))]
print(d)



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

shutil.copy(r'hw05_easy.py', r'hw05_easy_dupl.py')
