let marks = [85, 42, 76, 91, 38, 67, 55, 29, 80, 49];
let pcount = 0;
let fcount = 0;

for (let i = 0; i < marks.length; i++) {
    if (marks[i] >= 50) {
        console.log("Student " + (i + 1) + ": " +  marks[i] + " Pass");
        pcount++;
    } else {
        console.log("Student " + (i + 1) + ": " + marks[i] + " Fail");
        fcount++;
    }
}
console.log("Total Passed: " + pcount);
console.log("Total Failed: " + fcount);