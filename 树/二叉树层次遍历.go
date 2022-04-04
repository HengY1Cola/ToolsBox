package main

import (
	"fmt"
	"github.com/isdamir/gotype"
	"sort"
)

func printTreeLayer(root *gotype.BNode) {
	// todo 准备工作
	if root == nil {
		return
	}
	var temp *gotype.BNode
	queue := gotype.NewSliceQueue()
	queue.EnQueue(root)
	// todo 开始处理
	for !queue.IsEmpty() {
		temp = queue.DeQueue().(*gotype.BNode)
		fmt.Println(temp.Data)
		if temp.LeftChild != nil {
			queue.EnQueue(temp.LeftChild)
		}
		if temp.RightChild != nil {
			queue.EnQueue(temp.RightChild)
		}
	}
}

func toTree(array []int, start int, end int) *gotype.BNode {
	var rootNode *gotype.BNode
	if end >= start {
		rootNode = gotype.NewBNode()
		mid := (start + end + 1) / 2
		rootNode.Data = array[mid]
		rootNode.RightChild = toTree(array, mid+1, end)
		rootNode.LeftChild = toTree(array, start, mid-1)
	}
	return rootNode
}

func main() {
	intArray := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	sort.Ints(intArray)
	root := toTree(intArray, 0, len(intArray)-1)
	printTreeLayer(root)
}
