package main

import "github.com/isdamir/gotype"

func rollOver(head *gotype.LNode) {
	// todo 判断
	if head == nil || head.Next == nil {
		return
	}
	// todo 定义
	pre := head
	cur := head.Next
	var next *gotype.LNode
	// todo 开始翻转
	for cur != nil && cur.Next != nil {
		// 定义
		next = cur.Next.Next
		// 开始改变指针
		pre.Next = cur.Next
		cur.Next.Next = cur
		cur.Next = next
		// 准备进入下一个循环
		pre = cur
		cur = next
	}
}

func main() {
	head := &gotype.LNode{}
	gotype.CreateNode(head, 7)
	gotype.PrintNode("原始：", head)
	rollOver(head)
	gotype.PrintNode("现在：", head)
}
