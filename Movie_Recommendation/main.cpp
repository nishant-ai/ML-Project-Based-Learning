class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* temp1=headA;
        while(temp1!=NULL){
            ListNode* temp2=headB;
            while(temp2!=NULL){
                if (temp1==temp2) return temp1;
                temp2=temp2->next;
            }
            temp1=temp1->next;
        }
        
        return NULL;
    }
};