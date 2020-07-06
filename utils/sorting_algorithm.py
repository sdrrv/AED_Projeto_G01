import ctypes

class Sorting_Algorithm:
    def merge(self,arr, l, m, r): 
        n1 = m - l + 1
        n2 = r- m 

        L = (n1* ctypes.py_object)()
        R = (n2 * ctypes.py_object)() 
        
        for i in range(0 , n1): 
            L[i] = arr[l + i] 
        for j in range(0 , n2): 
            R[j] = arr[m + 1 + j] 
        i = 0     
        j = 0     
        k = l     
        while i < n1 and j < n2 : 
            if L[i] <= R[j]: 
                arr[k] = L[i] 
                i += 1
            else: 
                arr[k] = R[j] 
                j += 1
            k += 1
        while i < n1: 
            arr[k] = L[i] 
            i += 1
            k += 1
        while j < n2: 
            arr[k] = R[j] 
            j += 1
            k += 1

    def mergeSort(self,arr,l,r): 
        if l < r: 
            m = (l+(r-1))//2
            self.mergeSort(arr, l, m) 
            self.mergeSort(arr, m+1, r) 
            self.merge(arr, l, m, r)

    def sort(self,array_to_sort,size_of_the_array): # Unica para usar
        self.mergeSort(array_to_sort,0,size_of_the_array-1)
