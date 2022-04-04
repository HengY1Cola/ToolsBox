package main

import "github.com/isdamir/gotype"

// 删除指定节点
func deleteKeyNode(keyNode *gotype.LNode) {
	if keyNode == nil || keyNode.Next == nil { // 如果是尾节点就无法成功
		return
	}
	// todo 转移数据
	keyNode.Data = keyNode.Next.Data
	// todo 改变指针
	keyNode.Next = keyNode.Next.Next
}

// 找到指定节点
func findKeyNode(head *gotype.LNode, key int) *gotype.LNode {
	if head == nil || head.Next == nil {
		return nil
	}
	temp := head
	for i := 0; i < key; i++ {
		temp = temp.Next
		if temp == nil {
			return nil
		}
	}
	return temp
}

func main() {
	head := &gotype.LNode{}
	gotype.CreateNode(head, 8)
	gotype.PrintNode("原始：", head)
	keyNode := findKeyNode(head, 3)
	deleteKeyNode(keyNode)
	gotype.PrintNode("现在：", head)
}
