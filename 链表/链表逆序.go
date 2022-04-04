package main

import (
	"github.com/isdamir/gotype"
	"log"
)

// Reverse 就地逆序
func Reverse(node *gotype.LNode) {
	// todo 判断为空直接返回
	if node == nil || node.Next == nil {
		return
	}
	// todo 开始定义
	var pre *gotype.LNode
	var cur *gotype.LNode
	next := node.Next
	// todo 开始改变指针并且不断重新定义新的pre与cur
	for next != nil {
		cur = next.Next
		next.Next = pre
		pre = next
		next = cur
	}
	// todo 将头指针指向最后一个
	node.Next = pre
}

// InsertReverse 插入逆序
func InsertReverse(node *gotype.LNode) {
	// todo 判断
	if node == nil || node.Next == nil {
		log.Println(node.Next)
		return
	}
	// todo 定义
	var cur *gotype.LNode
	var next *gotype.LNode
	cur = node.Next.Next
	node.Next.Next = nil
	// todo 开始逆序
	for cur != nil {
		next = cur.Next
		cur.Next = node.Next
		node.Next = cur
		cur = next
	}

}

func main() {
	head := &gotype.LNode{}
	gotype.CreateNode(head, 8)
	gotype.PrintNode("原始：", head)
	Reverse(head)
	gotype.PrintNode("方式一： 就地逆序: ", head)
	head2 := &gotype.LNode{}
	gotype.CreateNode(head2, 8)
	InsertReverse(head2)
	gotype.PrintNode("方式二： 插入逆序: ", head2)
}
