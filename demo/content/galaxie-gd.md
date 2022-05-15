---
title: galaxie-gd
UID: 220502093439
created: 02-May-2022
tags:
  - 'created/2022/May/02'
  - 'garden'
  - 'permanent/concept'
aliases:
  - 
publish: False
---
# galaxie-gd

## Notes:

galaxie-gd là một sample dùng để publish githubpage từ markdown thành html theo phong cách zettelkasten.
galaxie-gd dựa trên template Telescope, build bằng npm.
fistime setup need to install dependancies
```
cd galaxie-gd
npm install
```

Steps to build
```
cd galaxie-gd
npm run build
npm run deploy
```

https://github.com/Greaby/galaxie-gd
https://github.com/Greaby/telescope

## Limitation
- [[📝22-05-02]]
	- YAML error with some type of data
		- ![[Pasted image 20220502100545.png]]
		- ![[Pasted image 20220502101511.png]]
			```
			D:\galaxie-gd\node_modules\slugify\slugify.js:20
		  throw new Error('slugify: string argument expected')
				^
	
			Error: slugify: string argument expected
			```
	- Only graph view only support auto link tags. Link notes must manual add YAML citation or quote to point to other file name.
	- Not support wikilinks type yet `[[]]`
		- Need to convert to markdown link first
	- Telescope convert unicode charater of filename to ASCII first and replace space ` ` by `-`. Linking has issue with space, unicode character
	- ...

## Ideas & thoughts:
- Template này chưa thực sự support good lắm cho Zettelkasten publish. Limitation khá nhiều, không autolink notes được. Được cái telecopes parse được cái [[Backlink Graph View]] khá đẹp, có thể ref để tự improve feature này cho mình.
- [[📝22-05-02]] Chốt: chưa dùng được, sẽ ref code telescope để làm graph view feature.

