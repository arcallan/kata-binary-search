// Binary search using iteration
// Run in console" "node kchop2.js"

// define function
function binsearch(arr, target, start, end) {
    var timer = 0;
    var maxit = Math.ceil((Math.log(end+1))/(Math.log(2))) + 1;
    while (timer < maxit) {
        mid = Math.floor((start + end)/2); // calculate midpoint of current range
        if (arr[mid] == target) { // check if midpoint is target
            return console.log("The target has index " + mid);
        }
        else if (arr[mid] > target) { // if target is in first half of range
            end = mid - 1;
        }
        else if (arr[mid] < target) { // if target is in second half of range
            start = mid + 1;
        }
        timer++;
    }
    return console.log("Target not in array");
}



var arr = [2, 3, 4, 10, 27, 40, 99, 212]; // define ordered list to search
//var target = 212; //define target
var len = arr.length; // find length of array

//binsearch(arr, target, 0, len-1);


// test function against all member of array
for (i in arr) {
    var target = arr[i];
    console.log(arr[i]);
    binsearch(arr, target, 0, len-1);
} 
