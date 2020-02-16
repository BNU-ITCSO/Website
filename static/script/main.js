function isIE() {
    return !!window.ActiveXObject || "ActiveXObject" in window;
}

if (isIE()) {
    alert("求求你不用IE好吗(T_T)\n可能会有各种比例不对等等问题\n可以试试Firefox,Chrome\n实在不行360都可以(✿◕‿◕✿)")
}