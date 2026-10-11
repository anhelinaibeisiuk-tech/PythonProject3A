import random


def generate_array(length: int, min_value: int, max_value: int) -> list[int]:
    """Генерує список цілих чисел заданої довжини в діапазоні [min_value, max_value]."""
    return [random.randint(min_value, max_value) for _ in range(length)]


def print_array(arr: list[int]) -> None:
    """Виводить масив у форматі: [[cell_0_value]; [cell_1_value]; ... [cell_n_value]]."""
    formatted_elements = "; ".join(f"[{x}]" for x in arr)
    print(f"[{formatted_elements}]")


def bubble_sort(arr: list[int], is_ascending: bool = True) -> list[int]:
    """
    Сортування бульбашкою (Bubble Sort).
    is_ascending = True  -> за зростанням
    is_ascending = False -> за спаданням
    """
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            should_swap = (a[j] > a[j + 1]) if is_ascending else (a[j] < a[j + 1])
            if should_swap:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def insertion_sort(arr: list[int], is_ascending: bool = True) -> list[int]:
    """
    Сортування вставками (Insertion Sort).
    is_ascending = True  -> за зростанням
    is_ascending = False -> за спаданням
    """
    a = arr.copy()
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and ((a[j] > key) if is_ascending else (a[j] < key)):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def selection_sort(arr: list[int], is_ascending: bool = True) -> list[int]:
    """
    Сортування вибором (Selection Sort).
    is_ascending = True  -> за зростанням
    is_ascending = False -> за спаданням
    """
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        target_idx = i
        for j in range(i + 1, n):
            is_better = (a[j] < a[target_idx]) if is_ascending else (a[j] > a[target_idx])
            if is_better:
                target_idx = j
        a[i], a[target_idx] = a[target_idx], a[i]
    return a


def main():
    print("=== ПРАКТИЧНА РОБОТА №3: ПРОСТІ АЛГОРИТМИ СОРТУВАННЯ ===\n")

    # 1. Bubble Sort
    print("--- 1. BUBBLE SORT (Сортування бульбашкою) ---")
    arr1 = generate_array(7, 10, 99)
    print("Початковий масив:       ", end="")
    print_array(arr1)

    print("Прямий порядок (True):  ", end="")
    print_array(bubble_sort(arr1, True))

    print("Зворотний порядок (False): ", end="")
    print_array(bubble_sort(arr1, False))
    print()

    # 2. Insertion Sort
    print("--- 2. INSERTION SORT (Сортування вставками) ---")
    arr2 = generate_array(8, 1, 50)
    print("Початковий масив:       ", end="")
    print_array(arr2)

    print("Прямий порядок (True):  ", end="")
    print_array(insertion_sort(arr2, True))

    print("Зворотний порядок (False): ", end="")
    print_array(insertion_sort(arr2, False))
    print()

    # 3. Selection Sort
    print("--- 3. SELECTION SORT (Сортування вибором) ---")
    arr3 = generate_array(6, -20, 20)
    print("Початковий масив:       ", end="")
    print_array(arr3)

    print("Прямий порядок (True):  ", end="")
    print_array(selection_sort(arr3, True))

    print("Зворотний порядок (False): ", end="")
    print_array(selection_sort(arr3, False))


if __name__ == "__main__":
    main()