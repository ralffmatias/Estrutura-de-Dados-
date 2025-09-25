import random
import datetime


# -------------------------------
# Classe de Ordenação
# -------------------------------
class Ordenacao:

    @staticmethod
    def bubble_sort(arr, key=lambda x: x, reverse=False):
        arr = arr.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if (key(arr[j]) > key(arr[j+1]) and not reverse) or (key(arr[j]) < key(arr[j+1]) and reverse):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    @staticmethod
    def quick_sort(arr, key=lambda x: x, reverse=False):
        if len(arr) <= 1:
            return arr
        pivot = key(arr[len(arr)//2])
        left = [x for x in arr if (key(x) < pivot and not reverse) or (key(x) > pivot and reverse)]
        middle = [x for x in arr if key(x) == pivot]
        right = [x for x in arr if (key(x) > pivot and not reverse) or (key(x) < pivot and reverse)]
        return Ordenacao.quick_sort(left, key, reverse) + middle + Ordenacao.quick_sort(right, key, reverse)

    @staticmethod
    def merge_sort(arr, key=lambda x: x, reverse=False):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = Ordenacao.merge_sort(arr[:mid], key, reverse)
        right = Ordenacao.merge_sort(arr[mid:], key, reverse)

        return Ordenacao._merge(left, right, key, reverse)

    @staticmethod
    def _merge(left, right, key, reverse):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if (key(left[i]) <= key(right[j]) and not reverse) or (key(left[i]) >= key(right[j]) and reverse):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


    @staticmethod
    def _heapify(arr, n, i, key, reverse):
        """Mantém a propriedade do heap para o nó i."""
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and ((key(arr[l]) > key(arr[largest]) and not reverse) or
                      (key(arr[l]) < key(arr[largest]) and reverse)):
            largest = l
        if r < n and ((key(arr[r]) > key(arr[largest]) and not reverse) or
                      (key(arr[r]) < key(arr[largest]) and reverse)):
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            Ordenacao._heapify(arr, n, largest, key, reverse)

    @staticmethod
    def heap_sort(arr, key=lambda x: x, reverse=False):
        """Ordena usando Heap Sort."""
        arr = arr.copy()
        n = len(arr)

        # Construção do Max-Heap / Min-Heap
        for i in range(n // 2 - 1, -1, -1):
            Ordenacao._heapify(arr, n, i, key, reverse)

        # Extração de elementos do heap
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            Ordenacao._heapify(arr, i, 0, key, reverse)

        return arr

