console.log("Hello World");
(async (table) => {
	console.log(table);

	// tr#gvStdList_ctl02
	// td#gvStdList_ctl02_lbClassName
	// td#gvStdList_ctl02_lbStdNo
	// td#gvStdList_ctl02_lbStdCName
	// td#gvStdList_ctl02_rblClass1_2

	async function fill( list ){
		for (i=2; ;i++) {
			let key="gvStdList_ctl"+(i<10?"0":"")+i;
				cell={
					"No":document.getElementById(key+"_lbStdNo"),
					"Name":document.getElementById(key+"_lbStdName"),
					"Class":document.getElementById(key+"_lbClassName")
				};
			if (cell.No) {
				cell={
					"No":((cell.No||{}).textContent||"").trim(),
					"Name":((cell.Name||{}).textContent||"").trim(),
					"Class":((cell.Class||{}).textContent||"").trim()
				}
				if (list.indexOf(cell.No)<0) continue
				if (!document.getElementById(key+"_rblClass1_3").checked)
					document.getElementById(key+"_rblClass1_2").click();
			} else break;
		}
	}
	table.parentNode.insertBefore(
		((blk)=>{
			blk.style.border="solid 3px blue";
			blk.appendChild(ipt=document.createElement("textarea"));
			ipt.style.width="98%";
			ipt.setAttribute("rows","6");
			ipt.setAttribute("placeholder","請貼上欲登錄曠課的學號清單");
			ipt.addEventListener("change",function(event){
				let list=(ipt.value||"").split(/[,; \n]/).filter((v)=>v);
				ipt.value=list.join("\n");
			});
			blk.appendChild(document.createElement("br"));
			blk.appendChild(btn=document.createElement("button"));
			btn.textContent="套用";
			btn.addEventListener("click",function(event){
				let list=(ipt.value||"").split(/[,; \n]/).filter((v)=>v);
				ipt.value=list.toString();
				fill(list);
				event.stopPropagation();
				event.preventDefault();
			});
			return blk;
		})(document.createElement("div")),
		table
	);

})(document.getElementById("gvStdList"));
