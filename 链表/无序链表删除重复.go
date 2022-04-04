package main

import (
	"github.com/isdamir/gotype"
)

// RemoveDup 顺序删除
func RemoveDup(head *gotype.LNode) {
	// todo 判断有没有必要
	if head == nil || head.Next == nil {
		return
	}
	// todo 申明变量
	outerCur := head.Next
	var innerCur *gotype.LNode
	var innerPre *gotype.LNode
	// 开始外内循环
	for ; outerCur != nil; outerCur = outerCur.Next {
		for innerCur, innerPre = outerCur.Next, outerCur; innerCur != nil; {
			if innerCur.Data == outerCur.Data { // 如果重复则删除
				innerPre.Next = innerCur.Next
				innerCur = innerCur.Next
			} else { // 如果重复则更新
				innerPre = innerCur
				innerCur = innerCur.Next
			}
		}
	}
}

// 创建重复链表
func createNode(node *gotype.LNode) {
	numList := [...]int{1, 2, 3, 2, 4, 7, 4, 6}
	max := 8
	cur := node
	for i := 0; i < max; i++ {
		cur.Next = &gotype.LNode{}
		cur.Next.Data = numList[i]
		cur = cur.Next
	}
}

func main() {
	head := &gotype.LNode{}
	createNode(head)
	RemoveDup(head)
	gotype.PrintNode("经过了顺序删除，结果为：", head)
}
