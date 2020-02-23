class Solution {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length <= 1) {
            if (nums2.length <= 1) {
                return Double.valueOf(nums1[0] + nums2[0] / 2);
            }
            else {
                return (Double.valueOf(nums1[0]) + medianHelper(nums2)) / 2;
            }
        }
        else if (nums2.length <= 1) {
            // System.out.println("Double value of nums2[0]: " + Double.valueOf(nums2[0]));
            return (Double.valueOf(nums2[0]) + medianHelper(nums1)) / 2;
        }
        // find median of first array
        double firstMedian = medianHelper(nums1);
        // find median of second array
        double secondMedian = medianHelper(nums2);
        // sum the two medians and divide by two
        return firstMedian + secondMedian / 2.0;

    }

    public static double medianHelper(int[] nums) {
        // helper function that returns the median value of the array
        if (nums.length % 2 != 0) {
            // odd length so just grab the middle value
            double halfVal = Double.valueOf(nums[nums.length / 2]);

            return halfVal;
        }
        else {
            // even length sum the two middle values and divide by two
            double val1 = Double.valueOf(nums[nums.length / 2 - 1]);
            double val2 = Double.valueOf(nums[nums.length / 2]);
            return (val1 + val2) / 2.0;
        }
    }

    public static void main(String args[]) {
        int [] nums1 = {1, 2, 3, 4, 5};
        int [] nums2 = {2};
        double median = findMedianSortedArrays(nums1, nums2);
        System.out.println("findMedianSortedArrays of [1, 2, 3, 4, 5] and [2]: " + median);
    }
}