package main

import (
	"fmt"
)

func isAfterOrder(arr []int, start int, end int) bool {
	if arr == nil {
		return false
	}
	root := arr[end] // 最后一个一定是根节点
	// todo 开始寻找第一个大于该循环中的根节点
	flag, index := 0, 0
	for i := start; i < end; i++ {
		if arr[i] > root {
			flag = i
			break
		}
	}
	// todo 判断是否满足规律
	for i := start; i < flag; i++ {
		if arr[i] > root {
			return false
		}
	}
	for index = flag; index < end; index++ {
		if arr[index] < root {
			return false
		}
	}
	leftFlag, rightFlag := true, true
	if start < flag {
		leftFlag = isAfterOrder(arr, start, flag-1)
	}
	if index < end {
		rightFlag = isAfterOrder(arr, flag, end)
	}
	return leftFlag && rightFlag
}

func main() {
	data := []int{1, 3, 2, 5, 7, 6, 4}
	res := isAfterOrder(data, 0, len(data)-1)
	fmt.Println(res)
}
