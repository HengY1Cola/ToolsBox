package main

import (
	"fmt"
	"github.com/isdamir/gotype"
)

// todo 构造环
func makeCircle(head *gotype.LNode, enter int) {
	// todo 判断成立
	if head == nil || head.Next == nil {
		return
	}
	// todo 标记入口
	key := head
	for i := 0; i < enter; i++ {
		if key == nil { // enter 无效
			return
		}
		key = key.Next
	}
	tail := head
	for {
		if tail.Next != nil {
			tail = tail.Next
		} else {
			break
		}
	}
	// todo 开始制造环
	tail.Next = key
}

// todo 检测环是否存在
func isLoop(head *gotype.LNode) *gotype.LNode {
	// todo 判断
	if head == nil || head.Next == nil {
		return nil
	}
	// todo 定义
	fast, slow := head.Next, head.Next
	// todo 开始跑
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
		if fast == slow {
			return fast
		}
	}
	return nil
}

// todo 找到入口点
func findLoopNode(head *gotype.LNode, meet *gotype.LNode) *gotype.LNode {
	// 因为要使用该函数的前提是已经知道了是环
	// todo 开始相遇
	key := head.Next
	for key != meet {
		key = key.Next
		meet = meet.Next
	}
	return key
}

func main() {
	head := &gotype.LNode{}
	gotype.CreateNode(head, 7)
	gotype.PrintNode("原始：", head)
	makeCircle(head, 3)
	res := isLoop(head)
	if res == nil {
		fmt.Println("无环")
	} else {
		fmt.Println("有环")
		res = findLoopNode(head, res)
		fmt.Println(res.Data)
	}
}
