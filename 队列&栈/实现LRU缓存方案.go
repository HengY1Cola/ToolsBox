package main

import (
	"fmt"
	"github.com/isdamir/gotype"
)

type LRU struct {
	CacheSize int
	Queue     gotype.SliceQueue
	Set       gotype.Set
}

// todo 判断是否满
func (l *LRU) isFull() bool {
	if l.Queue.Size() == l.CacheSize {
		return true
	} else {
		return false
	}
}

// todo 新来的如果满了则删除最后一个后加入第一个
func (l *LRU) enQueue(pageNum int) {
	if l.isFull() {
		l.Set.Remove(l.Queue.PopBack())
	}
	l.Queue.EnQueueFirst(pageNum)
	l.Set.Add(pageNum)
}

// todo 访问指定page不在则放入/在则移到队首
func (l *LRU) accessPage(pageNum int) {
	if !l.Set.Contains(pageNum) {
		l.enQueue(pageNum)
	} else {
		l.Queue.Remove(pageNum)
		l.Queue.EnQueueFirst(pageNum)
	}
}

// todo 打印

func (l *LRU) printLRU() {
	if l.Queue.IsEmpty() {
		return
	} else {
		for !l.Queue.IsEmpty() {
			fmt.Println(l.Queue.DeQueue())
		}
	}
}

func main() {
	oneLRU := &LRU{
		CacheSize: 4,
		Queue:     *gotype.NewSliceQueue(),
		Set:       *gotype.NewSet(),
	}
	oneLRU.accessPage(1)
	oneLRU.accessPage(3)
	oneLRU.accessPage(4)
	oneLRU.accessPage(6)
	oneLRU.accessPage(3)
	oneLRU.accessPage(7)
	oneLRU.printLRU()
}
