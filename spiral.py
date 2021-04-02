try:
    N = int(input("Введи число"))
except (ValueError, TypeError, IndexError):
    print('Это не число. Давай заново.')
else:
    if 4 <= N <= 1000:
        A = [[0]*N for i in range(N)] #матрица NxN
        m = 1 #счетчик чисел
        k = 0 #счетчик коэффициентов
        A[N//2][N//2] = N*N #если нечетное, если четное, то перезапишется

        for k in range (N//2):
            n = N-1-k*2
            for i in range (n):
                A[k][i+k] = m
                m +=1
            for i in range (n):
                A[k+i][N-k-1] = m
                m +=1
            for i in range (n):
                A[N-k-1][N-i-k-1] = m
                m +=1
            for i in range (n):
                A[N-i-k-1][k] = m
                m += 1
            k +=1

        for i in range(N):
            print(*A[i],sep='\t')

    else:print('не вместилось в диапазон')