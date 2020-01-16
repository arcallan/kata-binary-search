// Binary search using recursive function
// Run in console" "node kchop2.js"

// Definition of binary search function
function binsearch(arr, target, start, end) {
    mid = Math.floor((end+start)/2);
    if (arr[mid] == target) {
        return console.log("The target has index " + mid);
    }
    else if ((end - start) < 1) {
        return console.log("Target not found");
    }
    else if (arr[mid] < target) {
        return binsearch(arr, target, mid+1, end);
    }
    else if (arr[mid] > target) {
        return binsearch(arr, target, start, mid-1);
    }
    
}

var arr = [2, 3, 4, 10, 11, 27, 40, 99, 212];
var target = 11;
var len = arr.length;

// Function call
binsearch(arr, target, 0, len-1);
