package main

import (
	"fmt"
	"github.com/isdamir/gotype"
	"math"
)

type MiniStack struct {
	element *gotype.SliceStack
	mini    *gotype.SliceStack
}

func (s *MiniStack) push(data int) {
	s.element.Push(data)
	if s.mini.IsEmpty() {
		s.mini.Push(data)
	} else {
		if data <= s.mini.Top().(int) {
			s.mini.Push(data)
		}
	}
}

func (s *MiniStack) pop() {
	top := s.element.Pop()
	if top == s.mini.Top().(int) {
		s.mini.Pop()
	}
}

func (s *MiniStack) findMini() int {
	if s.mini.IsEmpty() {
		fmt.Println("最小值为：", math.MaxInt32)
		return math.MaxInt32
	} else {
		res := s.mini.Top().(int)
		fmt.Println("最小值为：", res)
		return res
	}
}

func main() {
	stack := MiniStack{
		element: &gotype.SliceStack{},
		mini:    &gotype.SliceStack{},
	}
	stack.push(5)
	stack.findMini()
	stack.push(6)
	stack.findMini()
	stack.push(2)
	stack.findMini()
	stack.pop()
	stack.findMini()
}
