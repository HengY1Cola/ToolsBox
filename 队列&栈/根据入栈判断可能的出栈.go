package main

import (
	"fmt"
	"github.com/isdamir/gotype"
)

func isPopSerial(push string, pop string) bool {
	// todo 判断长度是否正确
	if len(push) == 0 || len(pop) == 0 || len(push) != len(pop) {
		return false
	}
	// todo 准备工作
	pushRune, popRune := []rune(push), []rune(pop)
	pushIndex, popIndex := 0, 0
	oneStack := gotype.NewSliceStack()
	// todo 开始处理
	for pushIndex < len(push) {
		// todo 先压入进去
		oneStack.Push(pushRune[pushIndex])
		pushIndex++
		// todo 开始判断
		for !oneStack.IsEmpty() && oneStack.Top() == popRune[popIndex] {
			popIndex++
			oneStack.Pop()
		}
	}
	// todo 判断是否成功
	if oneStack.IsEmpty() && popIndex == len(pop) {
		return true
	}
	return false
}

func main() {
	push := "12345"
	//pop := "32541"
	pop := "53412"
	if isPopSerial(push, pop) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
