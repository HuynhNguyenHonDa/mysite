from matplotlib import pyplot as plt
import numpy as np
from django.shortcuts import render

def chart(request):
    plt.pie(x = np.array([10, 20, 50]), # giá trị của các nhóm
            labels = ['Nhóm A', 'Nhóm B', 'Nhóm C'], # Nhãn của các nhóm
            colors = ['red', 'blue', 'green'], # Màu sắc của các nhóm
            autopct = '%1.1f%%', # Format hiển thị giá trị %
            shadow = True
        )
    plt.title('Biểu đồ tròn tỷ lệ % của các nhóm')
    a = plt.show()
    return render(request, 'firstapp/dashboard.html', {'a': a})
