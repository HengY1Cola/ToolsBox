package main

import (
	"github.com/isdamir/gotype"
)

func RotateK(head *gotype.LNode, key int) {
	// todo 判断条件
	if head == nil || head.Next == nil {
		return
	}
	// todo 拿到长度
	lengthSheet := head
	length := 0
	for {
		if lengthSheet.Next != nil {
			length += 1
			lengthSheet = lengthSheet.Next
		} else {
			break
		}
	}
	// todo 处理循环
	realKey := key % length
	fast, slow := head, head
	for i := 0; i < realKey; i++ {
		fast = fast.Next
	}
	for {
		if fast.Next != nil {
			fast = fast.Next
			slow = slow.Next
		} else {
			break
		}
	}
	// todo 开始改变链接
	fast.Next = head.Next
	head.Next = slow.Next
	slow.Next = nil
}

func main() {
	head := &gotype.LNode{}
	gotype.CreateNode(head, 8)
	gotype.PrintNode("原始：", head)
	RotateK(head, 3)
	gotype.PrintNode("结果为：", head)
}
