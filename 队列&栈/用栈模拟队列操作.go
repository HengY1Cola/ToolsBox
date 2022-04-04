package main

import (
	"fmt"
	"github.com/isdamir/gotype"
)

type stackQueue struct {
	inStack  *gotype.SliceStack
	outStack *gotype.SliceStack
}

func (s *stackQueue) push(data int) {
	s.inStack.Push(data)
}

func (s *stackQueue) pop() int {
	if s.outStack.IsEmpty() {
		for !s.inStack.IsEmpty() {
			res := s.inStack.Pop().(int)
			s.outStack.Push(res)
		}
		res := s.outStack.Pop().(int)
		fmt.Println("出来的数为：", res)
		return res
	} else {
		res := s.outStack.Pop().(int)
		fmt.Println("出来的数为：", res)
		return res
	}
}

func main() {
	queue := &stackQueue{
		inStack:  &gotype.SliceStack{},
		outStack: &gotype.SliceStack{},
	}
	queue.push(5)
	queue.push(4)
	queue.pop()
	queue.pop()
}
