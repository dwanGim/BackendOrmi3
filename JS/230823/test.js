window.alert('hello world!');

// 주석은 요렇게
var a;
let b;

// const(상수 변수)는 초기화해줘야합니다.
const c = 3;

'use strict';  // 자바스크립트를 엄격모드에서 실행

valueA;        // 변수 키워드 생략은 엄격모드에서 에러발생!
var valueA;
var valueA;
let valueA;    // 재정의로 인한 에러발생!
// const my_name; // 초기화가 없어서 에러발생!

valueA = 1;
const my_name ="WADE";

if(true){ // -- 코드블록의 시작입니다. -- //

	let valueB = 'Hello!';
	const my_name ="WADE";       // 코드블록 밖의 my_name과 별개의 상수입니다.

} // -- 코드블록의 끝입니다. -- //

valueB = 'nice to meet you!';  // 변수 정의 이전에 값을 할당 할 수 없습니다!
let valueB = 'Hi!';            // 코드블록 안의 valueB와 별개의 변수입니다.

let str1 = 'hello';
let str2 = str1;
console.log(str2); // 'hello'

str1 = 'world';
console.log(str2); // str2에 할당된 값은 여전히 'hello' 입니다.


// let text = "Next level 제껴라 제껴라 제껴라";
// console.log(text.indexOf('level'));
// // 5

// console.log(text.indexOf('제껴라'));
// // 11
// console.log(text.indexOf('제껴라', 16));
// // 19

// console.log(text.indexOf('광야'));
// // -1

let text = "Next level 제껴라 제껴라 제껴라";
console.log(text.lastIndexOf('level'));
// 5

console.log(text.lastIndexOf('제껴라'));
// 19
console.log(text.lastIndexOf('제껴라', 16));
// 15

console.log(text.lastIndexOf('광야'));
// -1

