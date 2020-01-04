class Solution {
    vector<int> stack;
    vector<int> minstack;

public:
    void push(int value) {
        stack.push_back(value);
        if (minstack.size()==0)
        	minstack.push_back(value);
        else if (value <= min())
        {
            minstack.push_back(value);
        }
        		
    }
    void pop() {
        int val = top();
        stack.erase(stack.end()-1);    
        if (val==min())
        	minstack.erase(minstack.end()-1);
    }
    int top() {
        return stack[stack.size()-1];
    }
    int min() {
        return minstack[minstack.size()-1];
    }
};