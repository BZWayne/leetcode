class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a=str(l1.val); b= str(l2.val)
        next= l1.next
        while next:
          a=str(next.val)+a
          next= next.next
        next= l2.next
        while next:
          b= str(next.val)+b
          next= next.next
          
        c= str(int(a)+int(b))
        i= len(c)-1
        l3= ListNode(int(c[i]))
        next= l3
        while i:          
          i-=1
          ch= int(c[i])
          if next != None:
            next.next= ListNode(ch)          
            next= next.next
        return l3        
                
