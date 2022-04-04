#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
typedef int SDataType;
//链表的节点
typedef struct SListNode
{
	SDataType _data;
	struct SListNode* _PNext;
}Node, * PNode;
typedef struct SList       //封装了链表的结构
{
	PNode _pHead;//指向链表第一个节点
}SList;
struct SListNode* BuySListNode(SDataType data) {
	struct SListNode* p;
	p = (SListNode*)malloc(sizeof(struct SListNode));
	p->_data = data;
	p->_PNext = NULL;
	return p;
}
void SListInit(SList* s) {
	assert(s);
	s->_pHead = NULL;
}//链表初始化
void SListPushBack(SList* s, SDataType data) {
	//找链表最后一个节点
	assert(s);
	PNode pNewNode = BuySListNode(data);
	if (s->_pHead == NULL) {//链表没有节点的情况
		s->_pHead = pNewNode;
	}
	else {
		PNode pCur = s->_pHead;
		while (pCur->_PNext) {
			pCur = pCur->_PNext;
		}
		//让最后一个节点指向新节点
		pCur->_PNext = pNewNode;
	}
}//尾插
void SListPrint(SList* s) {             //打印链表
	assert(s);
	PNode pCur = s->_pHead;
	while (pCur) {
		printf("%d--->", pCur->_data);
		pCur = pCur->_PNext;
	}
	printf("\n");
}
PNode SListFind(SList* s, SDataType data) {
	assert(s);
	PNode pCur = s->_pHead;
	while (pCur) {
		if (pCur->_data == data) {
			return pCur;
		}
		pCur = pCur->_PNext;
	}
	return NULL;
}//查找
void  Makecircle(SList* s){
	assert(s);
	PNode pCur = s->_pHead;
	while (pCur->_PNext) {
		pCur = pCur->_PNext;
	}
	pCur->_PNext = s->_pHead;
}//造圆
void Merge(SList* p, SList* s) {
	assert(p);
	assert(s);
	PNode pCur = p->_pHead;
	while (pCur->_PNext) {
		pCur = pCur->_PNext;
	}
	pCur->_PNext = s->_pHead;
}//合并
void SListPrintNode(SListNode* f) {
	printf("%d", f->_data);
	printf("\n");
}
struct SListNode* getIntersectionNode(SListNode* _PaNext) {
	SListNode* head = _PaNext;//头部
	SListNode* f = _PaNext;
	SListNode* s = _PaNext;//快慢指针指向头部
	do {
		f = f->_PNext->_PNext;
		s = s->_PNext;
		if (f == NULL) {
			return NULL;//无环
		}
	} while (f!=s);
		f = head;
	while (f != s) {
			f = f->_PNext;
			s = s->_PNext;
		}
	return s;
}//找交点
int main() {
	SList p;
	SList s;
	SListInit(&p);
	SListPushBack(&p, 1);
	SListPushBack(&p, 2);
	SListPrint(&p);
	SListInit(&s);
	SListPushBack(&s, 3);
	SListPushBack(&s, 4);
	SListPushBack(&s, 5);
	SListPushBack(&s, 6);
	Makecircle(&s);
	Merge(&p, &s);
	SListPrintNode(getIntersectionNode(p._pHead));
}