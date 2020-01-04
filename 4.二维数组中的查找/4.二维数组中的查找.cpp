class Solution {
public:
    bool Find(int target, vector<vector<int> > array) {
        if(array[0].size()==0){
            return false;
        }
        int row = array.size() - 1;
        int col = 0;
        while(row > -1 && col < array[0].size()){
            int x = array[row][col];
            if (x==target)
            	return true;
            else if (x > target)
            	row--;
            else
            	col++;
        }
        return false;
    }
};