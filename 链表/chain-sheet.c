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
void SListInsert(PNode pos, SDataType data) {
	PNode pNewNode = NULL;
	if (pos == NULL) {
		return;
	}
	pNewNode = BuySListNode(data);

	pNewNode->_PNext = pos->_PNext;
	pos->_PNext = pNewNode;
}//插入
void SListErase(SList* s, PNode pos) {
	assert(s);
	if (pos == NULL || s->_pHead == NULL) {
		return;
	}
	if (pos == s->_pHead) {
		s->_pHead = pos->_PNext;
	}
	else {
		PNode pPrePos = s->_pHead;
		while (pPrePos && pPrePos->_PNext != pos) {
			pPrePos = pPrePos->_PNext;
		}
		pPrePos->_PNext = pos->_PNext;
	}
	free(pos);
}//删除给定pos位置的节点。
void SListPrint(SList* s) {             //打印链表
	assert(s);
	PNode pCur = s->_pHead;
	while (pCur) {
		printf("%d--->", pCur->_data);
		pCur = pCur->_PNext;
	}
	printf("\n");
}
int main() {
	SList s;
	SListInit(&s);
	SListPushBack(&s, 2);
	SListPushBack(&s, 3);
	SListPushBack(&s, 4);
	SListPushBack(&s, 5);
	SListPrint(&s);
	SListInsert(SListFind(&s,4),9);
	SListPrint(&s);
	SListErase(&s, SListFind(&s, 4));
	SListPrint(&s);
}