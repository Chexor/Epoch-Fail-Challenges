const fs = require('fs');
const path = require('path');

const dataFile = '.obsidian/plugins/obsidian-icon-folder/data.json';
const data = JSON.parse(fs.readFileSync(dataFile, 'utf8'));

// Helper to get all files
function walk(dir, filelist = []) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const dirFile = path.join(dir, file);
    if (fs.statSync(dirFile).isDirectory()) {
      filelist = walk(dirFile, filelist);
    } else {
      filelist.push(dirFile);
    }
  }
  return filelist;
}

const allFiles = walk('20_Wiki');
let changed = false;

for (const file of allFiles) {
  if (file.endsWith('.md')) {
    // Determine the expected icon
    let expectedIcon = 'LiFileText';
    
    // Check if it's an atlas
    if (file.includes('01_Atlas')) {
      expectedIcon = 'LiMap';
    } 
    // Check if it's an atom
    else if (file.includes('03_Atom')) {
      expectedIcon = 'LiAtom';
    }
    // Check if it's practice
    else if (file.includes('04_Practice')) {
      expectedIcon = 'LiCode2';
    }
    // Check if it's versus
    else if (file.includes('05_Versus')) {
      expectedIcon = 'LiScale';
    }
    
    // Check if it's currently missing or different
    if (!data[file] || data[file] !== expectedIcon) {
      data[file] = expectedIcon;
      changed = true;
      console.log(`Updated icon for ${file} to ${expectedIcon}`);
    }
  }
}

if (changed) {
  fs.writeFileSync(dataFile, JSON.stringify(data, null, 2), 'utf8');
  console.log('data.json updated successfully.');
} else {
  console.log('All 20_Wiki icons are already correct.');
}
