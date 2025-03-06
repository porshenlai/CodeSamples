(async (table)=>{
	let rows=table.querySelectorAll("tr"), results=[];
	for(let i=0; i<rows.length; i++){
		let cells=[
			rows[i].querySelector('[headers="CCMS_jGridView_TH_1"]'),
			rows[i].querySelector('[headers="CCMS_jGridView_TH_2"]'),
			rows[i].querySelector('[headers="CCMS_jGridView_TH_3"]')
		];
		if (!cells[0] || !cells[1] || !cells[2]) continue
		results.push({
			"NAME":cells[0].textContent,
			"VALUE":cells[1].textContent,
			"TIME":cells[2].textContent
		});
	}
	console.log("RESULT=",JSON.stringify(results));
})(document.getElementById("CCMS_jGridView"));
