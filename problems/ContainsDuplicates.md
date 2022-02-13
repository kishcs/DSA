## If Duplicate element is there, then return true
<pre>
public boolean containsDuplicate(int[] nums) {       
        HashSet<Integer> list = new HashSet<>();
        for(int i = 0; i < nums.length; i++) {
            /*if(list.contains(nums[i])) {
                return true;
            }
            list.add(nums[i]);*/
            if(!list.add(nums[i])) {
                return true;
            }
        }
        return false;
    }
   </pre>
