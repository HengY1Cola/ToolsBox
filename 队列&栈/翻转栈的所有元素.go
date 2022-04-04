package main

import (
	"fmt"
	"github.com/isdamir/gotype"
)

// todo 创建stack
func createStack(list []int) *gotype.SliceStack {
	stack := gotype.NewSliceStack()
	for _, value := range list {
		stack.Push(value)
	}
	return stack
}

// todo 读取Stack
func printStack(stack *gotype.SliceStack) {
	for !stack.IsEmpty() {
		fmt.Println(stack.Pop())
	}
}

// todo 将最下面的元素移到最上面
func moveButtonToTop(stack *gotype.SliceStack) {
	if stack.IsEmpty() {
		return
	}
	top1 := stack.Pop()
	if !stack.IsEmpty() {
		moveButtonToTop(stack)
		top2 := stack.Pop()
		stack.Push(top1)
		stack.Push(top2)
	} else {
		stack.Push(top1)
	}
}

func ReverseStack(stack *gotype.SliceStack) {
	if stack.IsEmpty() {
		return
	}
	moveButtonToTop(stack)
	top := stack.Pop()
	ReverseStack(stack)
	stack.Push(top)
}

func main() {
	oneStack := createStack([]int{5, 4, 3, 2, 1})
	ReverseStack(oneStack)
	printStack(oneStack)
}
