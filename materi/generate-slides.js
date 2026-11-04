const pptxgen = require('/tmp/pptx-tools/node_modules/pptxgenjs');
const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = 'Materi Pengantar Manajemen — Sub-CMPK 11';
pptx.subject = 'Menjelaskan Motivasi dalam Organisasi';
pptx.title = 'Pengantar Manajemen | Motivasi';
pptx.company = 'Bahan ajar berbasis RPS Pengantar Manajemen UNSRAT';
pptx.lang = 'id-ID';
pptx.theme = { headFontFace: 'Aptos Display', bodyFontFace: 'Aptos', lang: 'id-ID' };
pptx.defineSlideMaster({
  title: 'MASTER', background: { color: 'F7F8FA' },
  objects: [
    { rect: { x: 0, y: 0, w: 13.333, h: 0.15, line: { color: '0E7490', transparency: 100 }, fill: { color: '0E7490' } } },
    { line: { x: 0.55, y: 7.12, w: 12.23, h: 0, line: { color: 'DDE3E8', width: 0.8 } } },
    { text: { text: 'PENGANTAR MANAJEMEN  •  SUB-CMPK 11', options: { x: 0.58, y: 7.16, w: 7.0, h: 0.18, fontFace: 'Aptos', fontSize: 8, color: '60717D', charSpacing: 0.6, margin: 0 } } },
    { text: { text: 'UNSRAT  |  MINGGU 11', options: { x: 10.1, y: 7.16, w: 2.55, h: 0.18, align: 'right', fontFace: 'Aptos', fontSize: 8, color: '60717D', charSpacing: 0.5, margin: 0 } } }
  ],
  slideNumber: { x: 12.82, y: 7.14, color: '60717D', fontFace: 'Aptos', fontSize: 9 }
});
const C = {navy:'102A43', teal:'0E7490', turquoise:'DDF4F2', coral:'E76F51', gold:'F4B942', ink:'263746', muted:'60717D', white:'FFFFFF', pale:'EEF3F6', green:'2D8A68', red:'B64645', purple:'6750A4'};
function addText(slide, text, x,y,w,h, opts={}) { slide.addText(text,{x,y,w,h,fontFace:opts.fontFace||'Aptos',fontSize:opts.fontSize||16,color:opts.color||C.ink,bold:opts.bold||false,margin:opts.margin===undefined?0:opts.margin,breakLine: false,fit:'shrink',valign:opts.valign||'mid',align:opts.align||'left',paraSpaceAfterPt:opts.paraSpaceAfterPt||0,bullet:opts.bullet,transparency:opts.transparency,italic:opts.italic||false,isTextBox:true,...opts}); }
function base(title, kicker='KONSEP INTI') {
  const s=pptx.addSlide('MASTER');
  addText(s,kicker.toUpperCase(),0.62,0.36,6.0,0.24,{fontSize:9,bold:true,color:C.teal,charSpacing:1.1});
  addText(s,title,0.62,0.69,12.05,0.55,{fontSize:27,bold:true,color:C.navy,breakLine:false});
  return s;
}
function card(s,x,y,w,h,title,body,accent=C.teal,fs=15){
 s.addShape(pptx.ShapeType.roundRect,{x,y,w,h,rectRadius:0.08,fill:{color:C.white},line:{color:'E1E7EB',width:0.8},shadow:{type:'outer',color:'183247',blur:1.8,angle:45,distance:1,opacity:0.08}});
 s.addShape(pptx.ShapeType.rect,{x,y,w:0.07,h,fill:{color:accent},line:{color:accent,transparency:100}});
 addText(s,title,x+0.22,y+0.16,w-0.38,0.33,{fontSize:15,bold:true,color:accent});
 addText(s,body,x+0.22,y+0.55,w-0.4,h-0.68,{fontSize:fs,color:C.ink,valign:'top',breakLine:false,fit:'shrink',paraSpaceAfterPt:5});
}
function bullets(s,items,x,y,w,h,fs=19,color=C.ink){
 const txt=items.map(v=>({text:v,options:{bullet:{indent:fs*0.95},hanging:fs*0.22,breakLine:true}}));
 s.addText(txt,{x,y,w,h,fontFace:'Aptos',fontSize:fs,color,margin:0.04,breakLine:false,fit:'shrink',valign:'top',paraSpaceAfterPt:11,bullet:{indent:fs*0.95},hanging:fs*0.22});
}
function note(s, txt){s.addNotes(txt);}

// 1
{
 const s=pptx.addSlide(); s.background={color:C.navy};
 s.addShape(pptx.ShapeType.rect,{x:0,y:0,w:0.2,h:7.5,fill:{color:C.coral},line:{color:C.coral}});
 s.addShape(pptx.ShapeType.ellipse,{x:9.8,y:-0.7,w:4.3,h:4.3,fill:{color:'174A5B',transparency:10},line:{color:'174A5B',transparency:100}});
 s.addShape(pptx.ShapeType.ellipse,{x:10.8,y:4.5,w:3.3,h:3.3,fill:{color:'0E7490',transparency:28},line:{color:'0E7490',transparency:100}});
 addText(s,'PENGANTAR MANAJEMEN  /  MINGGU 11',0.8,0.82,8.8,0.3,{fontSize:12,bold:true,color:'78D5D0',charSpacing:1.4});
 addText(s,'MOTIVASI',0.8,1.65,9.2,0.92,{fontSize:48,bold:true,color:C.white});
 addText(s,'Memahami apa yang menggerakkan usaha\ndan bagaimana manajer menyalurkannya dengan adil',0.84,2.8,8.65,1.0,{fontSize:23,color:'E5EEF2',breakLine:false,valign:'top'});
 s.addShape(pptx.ShapeType.roundRect,{x:0.84,y:4.45,w:5.1,h:0.65,rectRadius:0.08,fill:{color:'174A5B'},line:{color:'174A5B'}});
 addText(s,'SUB-CMPK 11  •  “Menjelaskan motivasi”',1.05,4.62,4.7,0.25,{fontSize:13,bold:true,color:C.white});
 addText(s,'Berdasarkan RPS Pengantar Manajemen  |  S1 Manajemen',0.84,6.55,8.0,0.28,{fontSize:12,color:'C9D8DF'});
 note(s,'Pembuka (2 menit). Sampaikan bahwa materi ini merujuk Sub-CMPK minggu ke-11 dalam RPS: “Menjelaskan motivasi”, dengan cakupan pandangan motivasi dalam organisasi, model tradisional dan hubungan manusiawi, teori motivasi, proses penghargaan, pembentukan perilaku, serta teori keadilan. Tekankan bahwa motivasi dibahas sebagai konsep manajemen, bukan cara memberi label kepada orang. Tanyakan singkat: “Apa yang membuat Anda tetap berusaha ketika tugas kelompok terasa sulit?” Ambil dua jawaban sebagai pengantar, tanpa menilai jawaban sebagai benar atau salah.');
}
// 2
{
 const s=base('Apa yang akan Anda kuasai?','ARAH BELAJAR');
 card(s,0.65,1.55,3.82,2.0,'01  Menjelaskan','Intensitas, arah, dan ketekunan usaha dalam konteks organisasi.',C.teal,17);
 card(s,4.75,1.55,3.82,2.0,'02  Membedakan','Model tradisional, hubungan manusiawi, dan teori motivasi.',C.coral,17);
 card(s,8.85,1.55,3.82,2.0,'03  Menganalisis','Penghargaan, penguatan perilaku, dan persepsi keadilan.',C.purple,17);
 s.addShape(pptx.ShapeType.roundRect,{x:0.65,y:4.03,w:12.02,h:1.55,rectRadius:0.1,fill:{color:'E5F3F2'},line:{color:'D5ECE9'}});
 addText(s,'HASIL AKHIR',0.92,4.28,1.55,0.24,{fontSize:11,bold:true,color:C.teal,charSpacing:1});
 addText(s,'Usulkan tindakan manajerial yang etis, sesuai konteks, dan dapat dievaluasi.',2.36,4.22,9.85,0.55,{fontSize:22,bold:true,color:C.navy});
 addText(s,'Peta bahasan: kebutuhan → pilihan usaha → perilaku & hasil → penghargaan → evaluasi keadilan',0.82,5.98,11.7,0.4,{fontSize:15,bold:true,color:C.muted,align:'center'});
 note(s,'Jelaskan capaian sebagai perjalanan dari memahami konsep ke menerapkannya. Mahasiswa tidak hanya menyebut nama teori, tetapi harus menggunakan fakta kasus untuk menjelaskan mengapa suatu tindakan mungkin efektif atau tidak. Peta di bagian bawah adalah benang merah: kebutuhan dan konteks memengaruhi pilihan usaha; usaha dan perilaku menghasilkan konsekuensi; konsekuensi ditafsirkan kembali, termasuk apakah prosesnya adil. Beritahu bahwa di akhir sesi kelompok akan mengusulkan perbaikan untuk kasus kedai kopi.');
}
// 3
{
 const s=base('Motivasi bukan sekadar “semangat”','DASAR KONSEP');
 card(s,0.7,1.55,3.82,2.12,'INTENSITAS','Seberapa besar tenaga, fokus, atau usaha yang dicurahkan.',C.teal,18);
 card(s,4.75,1.55,3.82,2.12,'ARAH','Apakah usaha menuju tujuan dan standar yang tepat.',C.coral,18);
 card(s,8.8,1.55,3.82,2.12,'KETEKUNAN','Seberapa lama usaha dipertahankan saat ada hambatan.',C.purple,18);
 s.addShape(pptx.ShapeType.roundRect,{x:0.7,y:4.15,w:11.92,h:1.23,rectRadius:0.08,fill:{color:C.navy},line:{color:C.navy}});
 addText(s,'MOTIVASI ≠ KINERJA',0.98,4.4,2.55,0.34,{fontSize:17,bold:true,color:'78D5D0'});
 addText(s,'Kinerja juga dipengaruhi kemampuan, kejelasan peran, alat, waktu, dan dukungan.',3.55,4.35,8.55,0.48,{fontSize:18,bold:true,color:C.white});
 addText(s,'Tanya kelas: usaha tinggi tetapi salah sasaran—apakah hasilnya baik?',0.95,5.87,11.4,0.38,{fontSize:17,bold:true,color:C.teal,align:'center'});
 note(s,'Rujuk definisi Robbins dan Coulter: motivasi menjelaskan intensitas, arah, serta ketekunan usaha untuk mencapai tujuan. Tekankan arah—banyak usaha yang diarahkan ke target keliru tidak otomatis bermanfaat. Bedakan motivasi dari kinerja. Bila seseorang kekurangan pelatihan atau perangkat, motivasi saja tidak akan menyelesaikan hambatan. Beri waktu 30 detik untuk merespons pertanyaan di bawah; minta mahasiswa menyebut contoh usaha tinggi tetapi hasil kurang baik, misalnya memproses pesanan cepat namun sering salah.');
}
// 4
{
 const s=base('Dari mesin kerja ke manusia dalam sistem','PERKEMBANGAN PANDANGAN');
 card(s,0.72,1.52,5.82,3.38,'MODEL TRADISIONAL','• Taylor: standar, metode kerja, pengukuran\n• Insentif ekonomi dikaitkan dengan hasil\n• Kuat: efisiensi dan kejelasan target\n• Batas: manusia bukan hanya “penerima upah”',C.coral,17);
 card(s,6.78,1.52,5.82,3.38,'HUBUNGAN MANUSIAWI','• Relasi sosial, perhatian, kelompok kerja\n• Rasa diterima dan komunikasi ikut berpengaruh\n• Kuat: menyoroti pengalaman sosial\n• Batas: relasi baik tak menggantikan upah layak, keselamatan, dan desain kerja',C.teal,16);
 s.addShape(pptx.ShapeType.roundRect,{x:0.72,y:5.25,w:11.88,h:0.78,rectRadius:0.07,fill:{color:'E8E5F4'},line:{color:'E8E5F4'}});
 addText(s,'KINI: gabungkan kebutuhan, tujuan, keyakinan, konsekuensi, keadilan, dan konteks.',1.0,5.47,11.2,0.3,{fontSize:18,bold:true,color:C.purple,align:'center'});
 note(s,'Bandingkan dua pandangan yang diminta RPS. Model tradisional, terkait dengan manajemen ilmiah Taylor, menekankan rancangan kerja, standar dan insentif ekonomi. Jelaskan sumbangannya tanpa karikatur: pengukuran serta metode kerja dapat meningkatkan konsistensi. Kemudian model hubungan manusiawi memperluas fokus ke relasi, kelompok dan perhatian. Keduanya memiliki keterbatasan bila dipakai sendiri. Pandangan modern menggabungkan perspektif; tidak ada resep yang menjamin semua individu bereaksi sama. Dorong mahasiswa melihat pergeseran fokus dari “bagaimana membayar output” menuju “bagaimana membangun sistem kerja manusiawi dan efektif”.');
}
// 5
{
 const s=base('Tiga pertanyaan, tiga kelompok teori','PETA TEORI');
 card(s,0.72,1.55,3.82,3.5,'APA YANG DIANGGAP PENTING?','Teori kebutuhan / isi\n\nMaslow • ERG • Herzberg\nMcClelland',C.teal,18);
 card(s,4.75,1.55,3.82,3.5,'BAGAIMANA USAHA DIPILIH?','Teori proses\n\nHarapan (Vroom) • Tujuan\nKeadilan (Adams)',C.purple,18);
 card(s,8.78,1.55,3.82,3.5,'APA DAMPAK KONSEKUENSI?','Teori penguatan\n\nPenguatan operan\nPembentukan perilaku',C.coral,18);
 addText(s,'Gunakan teori sebagai lensa yang saling melengkapi—bukan “resep satu ukuran”.',0.9,5.74,11.6,0.42,{fontSize:18,bold:true,color:C.navy,align:'center'});
 note(s,'Ini peta untuk memudahkan ingatan. Teori isi atau kebutuhan menanyakan apa yang dianggap penting; teori proses menjelaskan penilaian tentang hubungan usaha, kinerja, dan hasil; teori penguatan meninjau bagaimana konsekuensi memengaruhi kemungkinan perilaku berulang. Keadilan dapat dikategorikan sebagai teori proses karena persepsi perbandingan memengaruhi respons. Tujuan teori bukan menentukan kepribadian seseorang, tetapi mengajukan pertanyaan diagnosis. Minta mahasiswa menyebut teori pada tiap kolom sebelum berpindah.');
}
// 6
{
 const s=base('Kebutuhan: Maslow dan ERG','TEORI ISI');
 const labels=[['FISIOLOGIS','kebutuhan dasar'],['KEAMANAN','aman & stabil'],['SOSIAL','relasi & rasa memiliki'],['PENGHARGAAN','pengakuan'],['AKTUALISASI','bertumbuh']];
 labels.forEach((a,i)=>{const x=0.77+i*2.48;const colors=['E7F4F3','D9EFED','C8E7E5','A9D7D3','79BBB7'];s.addShape(pptx.ShapeType.roundRect,{x,y:1.7,w:2.25,h:1.3,rectRadius:0.06,fill:{color:colors[i]},line:{color:colors[i]}});addText(s,a[0],x+0.06,1.92,2.13,0.25,{fontSize:11,bold:true,color:C.navy,align:'center'});addText(s,a[1],x+0.08,2.37,2.1,0.3,{fontSize:13,color:C.ink,align:'center'});});
 card(s,0.85,3.45,5.56,1.55,'MASLOW','Lima kelompok kebutuhan; gunakan sebagai lensa, bukan urutan universal yang kaku.',C.teal,16);
 card(s,6.65,3.45,5.56,1.55,'ERG (ALDERFER)','Existence • Relatedness • Growth\nBeberapa kebutuhan dapat aktif bersamaan.',C.purple,16);
 addText(s,'Manajer: tanyakan apa yang bernilai; pastikan kebutuhan dasar dan keselamatan tidak diabaikan.',0.9,5.66,11.6,0.47,{fontSize:17,bold:true,color:C.navy,align:'center'});
 note(s,'Uraikan lima kategori Maslow dengan contoh kerja, tetapi hindari mengklaim bahwa semua orang naik dalam urutan yang sama. ERG merangkum kebutuhan keberadaan, hubungan dan pertumbuhan; lebih memungkinkan beberapa kebutuhan aktif bersamaan. Gagasan frustrasi-regresi berarti kebutuhan lain dapat kembali penting saat peluang berkembang terhambat. Gunakan sebagai panduan bertanya: “Apa yang penting bagi Anda dalam tugas ini?” bukan sebagai label berdasarkan usia, jabatan atau latar belakang. Ingatkan bahwa gaji yang layak dan keselamatan adalah fondasi, bukan fasilitas motivasi mewah.');
}
// 7
{
 const s=base('Herzberg & McClelland: isi kerja dan kebutuhan','TEORI ISI');
 card(s,0.72,1.52,5.82,3.55,'HERZBERG: DUA FAKTOR','HIGIENE — kebijakan, supervisi, relasi, kondisi, imbalan; kekurangannya memicu ketidakpuasan.\n\nMOTIVATOR — pencapaian, pengakuan, tanggung jawab, kemajuan, makna kerja.',C.coral,16);
 card(s,6.78,1.52,5.82,3.55,'MCCLELLAND: KEBUTUHAN YANG DIPELAJARI','PRESTASI — tantangan & umpan balik\nAFILIASI — hubungan kooperatif\nPENGARUH — memengaruhi keputusan\n\nArahkan pengaruh untuk kepentingan tim.',C.teal,16);
 addText(s,'Perbaiki konteks kerja, lalu perkaya tugas—jangan memberi label permanen pada orang.',0.85,5.65,11.65,0.42,{fontSize:17,bold:true,color:C.navy,align:'center'});
 note(s,'Pada Herzberg, higiene membantu mencegah atau mengurangi ketidakpuasan; memenuhi faktor tersebut tidak otomatis membuat pekerjaan sangat memotivasi. Motivator berkaitan dengan isi pekerjaan dan pencapaian. Jangan gunakan teori untuk membenarkan upah rendah atau kondisi tidak aman. McClelland menyebut kebutuhan prestasi, afiliasi dan kekuasaan/pengaruh. Contoh-contoh di layar adalah kecenderungan yang mungkin, bukan tes diagnosis atau label tetap. Manajer dapat menawarkan variasi tugas, kesempatan kontribusi, umpan balik dan pengembangan, lalu mengamati apa yang membantu individu maupun tim.');
}
// 8
{
 const s=base('Teori harapan: apakah tiga mata rantai tersambung?','TEORI PROSES');
 const xs=[0.8,4.8,8.8], heads=['HARAPAN','INSTRUMENTALITAS','VALENSI'], q=['“Bisakah usaha menjadi kinerja?”','“Apakah kinerja menghasilkan janji?”','“Apakah hasil itu saya hargai?”'], colors=[C.teal,C.purple,C.coral];
 for(let i=0;i<3;i++){s.addShape(pptx.ShapeType.roundRect,{x:xs[i],y:1.78,w:3.65,h:2.0,rectRadius:0.1,fill:{color:C.white},line:{color:'DFE6EA'}});addText(s,heads[i],xs[i]+0.2,2.0,3.25,0.3,{fontSize:16,bold:true,color:colors[i],align:'center'});addText(s,q[i],xs[i]+0.25,2.56,3.15,0.65,{fontSize:18,bold:true,color:C.navy,align:'center'});}
 addText(s,'USAHA  →  KINERJA  →  HASIL YANG BERNILAI',1.15,4.28,11.0,0.55,{fontSize:24,bold:true,color:C.navy,align:'center'});
 addText(s,'Alat bantu: M ≈ E × I × V. Jika satu mata rantai terasa nol, motivasi melemah.',1.0,5.25,11.3,0.42,{fontSize:17,color:C.ink,align:'center'});
 note(s,'Jelaskan model Vroom dengan alur usaha menuju kinerja, kinerja menuju hasil, lalu nilai hasil. Tanyakan contoh hambatan per tiap mata rantai: pelatihan atau alat yang kurang melemahkan harapan; janji bonus yang berubah-ubah melemahkan instrumentalitas; penghargaan yang tidak diinginkan melemahkan valensi. Persamaan hanyalah mnemonic konseptual, bukan skor kuantitatif baku. Dalam kasus manajemen, bantu orang mampu berhasil, tepati hubungan kinerja-penghargaan, dan cari tahu hasil apa yang benar-benar bernilai. Jangan merespons semua masalah dengan menambah bonus.');
}
// 9
{
 const s=base('Tujuan jelas, menantang—dan tetap sehat','TEORI PROSES');
 card(s,0.78,1.6,5.55,2.55,'TUJUAN YANG MEMBANTU','• Spesifik dan cukup menantang\n• Ada komitmen, kemampuan, sumber daya\n• Umpan balik dan ukuran yang dipahami',C.teal,17);
 card(s,6.65,1.6,5.55,2.55,'PAGAR MUTU & ETIKA','• Jangan hanya mengukur kuantitas\n• Lindungi mutu, keselamatan, kepatuhan\n• Tugas kompleks mungkin perlu tujuan belajar',C.coral,17);
 s.addShape(pptx.ShapeType.roundRect,{x:0.82,y:4.65,w:11.3,h:0.92,rectRadius:0.08,fill:{color:'E6E2F2'},line:{color:'E6E2F2'}});
 addText(s,'Contoh: turunkan waktu respons 12 → 8 jam, tanpa penurunan kepuasan; tinjau mingguan.',1.03,4.9,10.9,0.36,{fontSize:17,bold:true,color:C.purple,align:'center'});
 addText(s,'Otonomi • kompetensi • keterhubungan turut menopang motivasi intrinsik.',0.9,5.93,11.5,0.35,{fontSize:16,bold:true,color:C.navy,align:'center'});
 note(s,'Ringkas teori penetapan tujuan: sasaran yang jelas dan menantang dapat membantu jika komitmen, kapasitas, sumber daya dan umpan balik tersedia. Untuk pekerjaan baru atau rumit, target hasil sempit dapat membuat orang mengejar angka tanpa belajar; tujuan belajar dan dukungan mungkin lebih tepat. Contoh target sengaja memasangkan kecepatan dengan kepuasan sebagai pagar mutu. Hubungkan motivasi intrinsik dengan dukungan otonomi, kompetensi dan keterhubungan: beri ruang memilih cara, umpan balik yang membantu, dan relasi yang saling menghormati.');
}
// 10
{
 const s=base('Pembentukan perilaku: konsekuensi membentuk kebiasaan','PENGUATAN');
 card(s,0.72,1.48,5.82,1.62,'PENGUATAN POSITIF  ↑','Tambahkan sesuatu yang dihargai setelah perilaku tepat.\nContoh: apresiasi spesifik atas pemeriksaan keselamatan.',C.green,15);
 card(s,6.78,1.48,5.82,1.62,'PENGUATAN NEGATIF  ↑','Hilangkan kondisi tidak menyenangkan setelah perilaku tepat.\nContoh: hapus pemeriksaan ganda yang tak perlu setelah konsistensi terbukti.',C.teal,14);
 card(s,0.72,3.45,5.82,1.62,'HUKUMAN  ↓','Konsekuensi untuk menurunkan perilaku; proporsional, jelas, dan disertai pembinaan.',C.red,15);
 card(s,6.78,3.45,5.82,1.62,'PEMADAMAN  ↓','Hentikan penguatan yang mempertahankan perilaku; tangani kebutuhan komunikasi yang sah.',C.purple,14);
 addText(s,'INGAT: penguatan negatif bukan hukuman—perilaku sasaran justru meningkat.',0.8,5.58,11.75,0.42,{fontSize:18,bold:true,color:C.red,align:'center'});
 note(s,'Tinjau empat konsekuensi dan arah perubahan yang diharapkan. Panah naik berarti perilaku sasaran meningkat; turun berarti berkurang. Perbedaan penting adalah reinforcement selalu meningkatkan perilaku sasaran, sedangkan punishment bertujuan menurunkannya. Penguatan negatif bukan berarti “negatif” secara moral; ia menghilangkan kondisi tidak menyenangkan setelah perilaku yang diharapkan sehingga perilaku itu meningkat. Contoh pemeriksaan ganda hanya tepat jika prosedur itu memang tidak perlu dan keselamatan tetap terjaga. Hukuman harus proporsional dan adil; lebih baik juga mengajarkan serta memperkuat perilaku alternatif yang benar.');
}
// 11
{
 const s=base('Keadilan: orang membandingkan kontribusi dan hasil','TEORI ADAMS');
 s.addShape(pptx.ShapeType.roundRect,{x:0.9,y:1.55,w:11.5,h:1.0,rectRadius:0.08,fill:{color:C.navy},line:{color:C.navy}});
 addText(s,'KONTRIBUSI (waktu, usaha, keterampilan)  ↔  HASIL (upah, jadwal, pengakuan, peluang)',1.15,1.83,11.0,0.4,{fontSize:19,bold:true,color:C.white,align:'center'});
 card(s,0.8,3.02,3.72,1.65,'DISTRIBUTIF','Apakah pembagian hasil terasa wajar?',C.teal,15);
 card(s,4.8,3.02,3.72,1.65,'PROSEDURAL','Apakah proses dan kriteria konsisten?',C.purple,15);
 card(s,8.8,3.02,3.72,1.65,'INTERAKSIONAL','Apakah orang dihormati & dijelaskan?',C.coral,15);
 addText(s,'Adil tidak selalu berarti sama. Perbedaan perlu alasan relevan, konsisten, dan transparan.',0.85,5.42,11.65,0.48,{fontSize:17,bold:true,color:C.navy,align:'center'});
 note(s,'Jelaskan teori keadilan Adams sebagai persepsi perbandingan rasio kontribusi-hasil dengan pihak pembanding yang dianggap relevan. Orang dapat merespons rasa tidak adil dengan mengubah usaha, meminta perubahan, menilai ulang pembanding, atau menarik diri; ini kemungkinan, bukan prediksi pasti. Perkenalkan tiga lapis praktis: distributif (hasil), prosedural (proses), interaksional (perlakuan dan penjelasan). Tidak semua orang harus menerima hasil identik, tetapi perbedaan harus punya dasar yang relevan, konsisten, dan dapat dijelaskan. Ajak kelas membedakan “hasil yang berbeda” dari “proses yang tidak adil”.');
}
// 12
{
 const s=base('Penghargaan efektif bila rantainya dipercaya','PENGHARGAAN');
 const steps=[['1','PERILAKU','target jelas'],['2','UKURAN','dapat dipercaya'],['3','PROSES','transparan'],['4','HASIL','bernilai'],['5','EVALUASI','cek efek samping']];
 steps.forEach((v,i)=>{let x=0.67+i*2.55;s.addShape(pptx.ShapeType.ellipse,{x:x+0.68,y:1.75,w:0.58,h:0.58,fill:{color:[C.teal,C.purple,C.coral,C.gold,C.green][i]},line:{color:[C.teal,C.purple,C.coral,C.gold,C.green][i]}});addText(s,v[0],x+0.68,1.91,0.58,0.18,{fontSize:15,bold:true,color:C.white,align:'center'});addText(s,v[1],x,2.54,1.95,0.3,{fontSize:13,bold:true,color:C.navy,align:'center'});addText(s,v[2],x,2.96,1.95,0.45,{fontSize:13,color:C.muted,align:'center'});if(i<4)addText(s,'→',x+1.95,1.88,0.48,0.28,{fontSize:22,bold:true,color:C.muted,align:'center'});});
 card(s,0.9,3.78,5.55,1.55,'FINANSIAL','Gaji/upah • bonus/komisi • manfaat',C.teal,16);
 card(s,6.75,3.78,5.55,1.55,'NONFINANSIAL','Pengakuan • fleksibilitas • belajar • makna',C.coral,16);
 addText(s,'Kompensasi layak, keselamatan, dan martabat adalah fondasi—bukan “bonus motivasi”.',0.8,5.78,11.75,0.45,{fontSize:16,bold:true,color:C.navy,align:'center'});
 note(s,'Gunakan diagram rantai untuk memeriksa desain penghargaan. Harus jelas perilaku atau hasil yang dihargai; datanya dapat dipercaya; kriteria konsisten; hasil bernilai; dan ada evaluasi dampak samping. Penghargaan dapat finansial langsung, tidak langsung, dan nonfinansial. Tidak ada bentuk yang otomatis paling baik. Satu ukuran volume dapat mendorong kesalahan atau mengorbankan layanan; seimbangkan dengan indikator mutu dan keselamatan. Tekankan etika: kompensasi layak dan kondisi aman tidak boleh diperlakukan sebagai hadiah untuk kelompok tertentu. Lindungi privasi dan jangan mempermalukan pekerja lewat papan peringkat tanpa persetujuan.');
}
// 13
{
 const s=base('Diagnosis manajer: cari hambatan sebelum menyalahkan','APLIKASI');
 const steps=[['1','Fakta','Apa yang berubah?'],['2','Kondisi','Alat, waktu, kemampuan?'],['3','Harapan','Usaha → kinerja → hasil?'],['4','Keadilan','Kriteria & perlakuan?'],['5','Tindakan','Dukungan + intervensi'],['6','Tinjau','Indikator & efek samping']];
 steps.forEach((v,i)=>{const col=i%3,row=Math.floor(i/3),x=0.78+col*4.13,y=1.56+row*1.8;card(s,x,y,3.72,1.48,`${v[0]}  ${v[1]}`,v[2],[C.teal,C.coral,C.purple,C.gold,C.green,C.red][i],16);});
 addText(s,'Gunakan percakapan dua arah. Motivasi tidak dapat didiagnosis dari satu angka.',0.8,5.65,11.8,0.45,{fontSize:18,bold:true,color:C.navy,align:'center'});
 note(s,'Berikan urutan diagnosis yang bisa dipakai dalam organisasi. Mulai dari data perilaku yang relevan, bukan asumsi karakter. Cek kondisi kerja dan kemampuan sebelum menyimpulkan motivasi. Tanyakan mata rantai harapan serta persepsi keadilan. Pilih tindakan yang sesuai—pelatihan, alat, tujuan yang lebih jelas, pengakuan, desain ulang tugas, atau koreksi proporsional—dan sepakati indikator. Minta mahasiswa melihat bahwa ini bukan formula mekanis: percakapan pribadi, konteks dan dampak samping penting. Satu metrik produktivitas tidak cukup untuk menyimpulkan kondisi motivasi.');
}
// 14
{
 const s=base('Kasus: Kopi Pesisir','DISKUSI KASUS');
 card(s,0.78,1.52,5.72,3.75,'APA YANG TERJADI?','Kedai memberi bonus mingguan berdasarkan jumlah pesanan.\n\nPesanan tercatat naik, tetapi salah pesanan dan jadwal mendadak ikut meningkat. Barista senior merasa pelatihan rekan tidak dihargai. Pegawai baru kurang terlatih. Rumus bonus tidak tertulis; sebagian tim lebih menghargai jadwal pasti.',C.coral,16);
 card(s,6.82,1.52,5.72,3.75,'TANTANGAN MANAJER','Jangan langsung menyebut orang “malas”.\n\nGunakan minimal 3 lensa: harapan, keadilan, penguatan, tujuan, Herzberg, atau kebutuhan. Rancang perbaikan 30 hari yang menjaga kecepatan sekaligus mutu.',C.teal,16);
 addText(s,'PEMICU: Apa yang diperkuat sistem saat ini—dan apa yang tanpa sengaja dikorbankan?',0.84,5.72,11.7,0.45,{fontSize:17,bold:true,color:C.navy,align:'center'});
 note(s,'Bacakan studi kasus ilustratif. Tekankan bahwa target bonus hanya berdasarkan jumlah membuat perilaku volume mudah terlihat, tetapi mungkin menurunkan akurasi dan kualitas pengalaman pelanggan. Ada isu expectancy karena pegawai baru belum terlatih; instrumentality karena rumus tak tertulis; valensi karena preferensi penghargaan berbeda; keadilan karena kerja melatih rekan tidak diakui; dan tujuan yang tidak seimbang. Minta mahasiswa mengidentifikasi fakta, bukan menebak motif. Pertanyaan pemicu mengarahkan mereka melihat konsekuensi yang mungkin diperkuat sistem.');
}
// 15
{
 const s=base('Kerja kelompok: usulkan uji coba 30 hari','AKTIVITAS KELAS');
 const items=[['A','Diagnosis','3 isu berbasis fakta'],['B','Teori','3 lensa + bukti'],['C','Rencana','tindakan dan penanggung jawab'],['D','Ukuran','2–3 indikator + efek samping']];
 items.forEach((v,i)=>{let x=0.82+(i%2)*6.1,y=1.55+Math.floor(i/2)*1.75;card(s,x,y,5.55,1.42,`${v[0]}  ${v[1]}`,v[2],[C.teal,C.purple,C.coral,C.green][i],17);});
 s.addShape(pptx.ShapeType.roundRect,{x:0.88,y:5.25,w:11.5,h:0.75,rectRadius:0.08,fill:{color:'FFF1D6'},line:{color:'F3E4C2'}});
 addText(s,'Presentasi 2 menit per kelompok • Nilai: konsep, bukti, kelayakan, etika',1.05,5.47,11.15,0.28,{fontSize:16,bold:true,color:C.navy,align:'center'});
 note(s,'Instruksi (sekitar 5 menit persiapan, 2 menit per kelompok sesuai jumlah kelompok). Minta kelompok membagi peran: pencatat fakta, penghubung teori, perancang intervensi, dan penyaji. Rencana harus menjelaskan langkah serta siapa yang bertanggung jawab, bukan sekadar “tingkatkan motivasi”. Minta indikator yang seimbang—misalnya salah pesanan, waktu respons, kepastian jadwal, dan persepsi keadilan agregat. Bahas pula privasi, beban kerja dan potensi efek samping. Gunakan rubrik di materi dosen: ketepatan konsep, bukti/diagnosis, kelayakan, pengukuran, etika/komunikasi.');
}
// 16
{
 const s=base('Cek pemahaman: jawab dalam 60 detik','ASESMEN FORMATIF');
 card(s,0.78,1.52,5.72,1.52,'1  Penguatan negatif?','Apa bedanya dengan hukuman?',C.teal,18);
 card(s,6.82,1.52,5.72,1.52,'2  Harapan melemah?','Pegawai tak punya alat. Apa intervensi pertama?',C.purple,18);
 card(s,0.78,3.45,5.72,1.52,'3  Keadilan?','Mengapa bonus sama belum tentu terasa adil?',C.coral,17);
 card(s,6.82,3.45,5.72,1.52,'4  Risiko target?','Apa yang terjadi jika hanya jumlah diukur?',C.red,17);
 addText(s,'Jawaban inti: naik vs turun perilaku • dukungan alat • proses & kontribusi • mutu/etika',0.8,5.55,11.8,0.5,{fontSize:15,bold:true,color:C.navy,align:'center'});
 note(s,'Gunakan sebagai exit ticket lisan atau tulisan. Beri satu menit untuk jawaban individu, lalu minta pasangan saling memeriksa. Kunci: penguatan negatif menghilangkan kondisi tidak menyenangkan dan meningkatkan perilaku sasaran; hukuman bertujuan menurunkannya. Tanpa alat, intervensi relevan adalah memperbaiki sumber daya/pelatihan dan harapan usaha-kinerja. Bonus sama belum tentu adil karena kontribusi, pembanding dan proses juga dipertimbangkan. Ukuran jumlah saja dapat mendorong salah mutu, jalan pintas, turunnya kerja sama atau kelelahan. Catat miskonsepsi untuk tindak lanjut.');
}
// 17
{
 const s=base('Inti yang perlu dibawa pulang','PENUTUP');
 const lines=[['01','Motivasi punya intensitas, arah, dan ketekunan.'],['02','Kinerja juga membutuhkan kemampuan dan dukungan.'],['03','Teori berbeda membantu mendiagnosis bagian yang berbeda.'],['04','Penghargaan harus bernilai, dipercaya, adil, dan etis.']];
 lines.forEach((v,i)=>{const y=1.47+i*0.86;s.addShape(pptx.ShapeType.ellipse,{x:1.0,y:y+0.04,w:0.42,h:0.42,fill:{color:[C.teal,C.purple,C.coral,C.green][i]},line:{color:[C.teal,C.purple,C.coral,C.green][i]}});addText(s,v[0],1.0,y+0.16,0.42,0.15,{fontSize:10,bold:true,color:C.white,align:'center'});addText(s,v[1],1.65,y,10.4,0.5,{fontSize:20,bold:i===3,color:C.navy});});
 s.addShape(pptx.ShapeType.roundRect,{x:0.9,y:5.25,w:11.4,h:0.62,rectRadius:0.08,fill:{color:C.navy},line:{color:C.navy}});
 addText(s,'Bacaan inti: Robbins & Coulter • Schermerhorn • Stoner & Wankel',1.15,5.43,10.9,0.25,{fontSize:14,bold:true,color:C.white,align:'center'});
 addText(s,'Terima kasih • Pertanyaan / refleksi',0.9,6.15,11.4,0.4,{fontSize:21,bold:true,color:C.teal,align:'center'});
 note(s,'Tutup dengan mengulang empat pesan utama. Motivasi terdiri atas intensitas, arah dan ketekunan; kinerja juga bergantung kemampuan dan dukungan. Teori kebutuhan, proses, penguatan dan keadilan menjawab pertanyaan yang berbeda sehingga manajer sebaiknya menggunakan beberapa lensa. Sistem penghargaan yang baik harus jelas, konsisten, bernilai dan tidak mengorbankan mutu atau martabat. Bacaan inti mengikuti daftar RPS; rujukan lengkap, termasuk karya klasik, tersedia dalam modul pendamping. Akhiri dengan refleksi: “Satu perubahan apa yang akan Anda rekomendasikan pada sistem Kopi Pesisir, dan bagaimana Anda tahu perubahan itu berhasil?”');
}

if (pptx._slides.length > 18) throw new Error('Maksimum 18 slide terlampaui: '+pptx._slides.length);
pptx.writeFile({fileName:'materi/slide-motivasi-sub-cmpk-11.pptx'});
