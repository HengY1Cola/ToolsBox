package main

import (
	"fmt"
	"github.com/isdamir/gotype"
)

func makeCross(length int, key int) (*gotype.LNode, *gotype.LNode) {
	// todo 保证length比key大
	if length < key {
		return nil, nil
	}
	// todo 创建对应的2条
	head1 := &gotype.LNode{}
	gotype.CreateNode(head1, length+1)
	head2 := &gotype.LNode{}
	gotype.CreateNode(head2, key+1)
	// todo 拿到head2尾节点与交叉节点
	cur1 := head1
	cur2 := head2
	for {
		if cur2.Next != nil {
			cur1 = cur1.Next
			cur2 = cur2.Next
		} else {
			cur2.Next = cur1.Next
			break
		}
	}
	return head1, head2
}

func isCross(head1 *gotype.LNode, head2 *gotype.LNode) bool {
	tail := head1
	for {
		if tail.Next != nil {
			tail = tail.Next
		} else {
			tail.Next = head2
			break
		}
	}
	fast, slow := head1.Next, head1.Next
	for {
		if fast.Next != nil && fast != nil {
			fast = fast.Next.Next
			slow = slow.Next
			if fast == slow {
				return true
			}
		} else {
			return false
		}
	}
}

func main() {
	head1, head2 := makeCross(7, 4) // 懒得判断为空了
	isCross := isCross(head1, head2)
	fmt.Println(isCross)
}
