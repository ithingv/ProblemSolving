from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    """삽입정렬을 사용해 리스트의 원소를 정렬"""

    for i in range(1, len(arr)):
        
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
        # 기존 배열 내에서 이동해야 하므로 
        # key를 삽입할 공간을 만들어주기 위해 다음 원소의 위치를 이동시켜야한다.
            arr[j+1] = arr[j]
            j -= 1
        # 처음으로 키보다 작은 값이 나왔을 때 그 값의 다음 위치에 key를 삽입
        arr[j+1] = key

    return arr