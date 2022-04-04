package main

import (
	"fmt"
	"github.com/isdamir/gotype"
)

// FindLastKey 采用快慢指针的方法
func FindLastKey(head *gotype.LNode, key int) *gotype.LNode {
	// todo判断是否成立
	fast := head
	for i := 0; i < key; i++ {
		fast = fast.Next
	}
	if head == nil || fast == nil {
		return nil
	}
	// 开始一起往前走
	slow := head
	for {
		if fast.Next != nil {
			fast = fast.Next
			slow = slow.Next
		} else {
			return slow.Next
		}
	}
}

func main() {
	head := &gotype.LNode{}
	gotype.CreateNode(head, 8)
	gotype.PrintNode("原始：", head)
	key := 3
	res := FindLastKey(head, key)
	fmt.Println("最后的结果为：", res.Data)
}
