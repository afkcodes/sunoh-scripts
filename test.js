// const { cipher, util } = require('node-forge');

// const key = '38346591';
// const iv = '00000000';

// const encrypted = util.decode64(
//   'https://ac.cf.saavncdn.com/236/9ebfe6a48e705e01616cddc50bce980a_160.mp4?Expires=1691330868&Signature=F2bfCw0p~E6tx~xpGcowzsFhsaDP6a8vYfDrnl~HBzOvVVZoY-MTQmRqH77opemM6JhU4gisGNWZ9Y2vP2mBCN-qoyEr~1TBMWtoio~FNucO6JDbL0dgxCUtQ0JLndxgTIorN7Y41K9kNb~L9ptgkMc4Dr93ptHO0OEYkgcDYO1B0be0lAd5L7yiFQ8rxxcjgV32ZYmq7cpTO1U3cg9zsVm7~dK5t-GgGV2UnE0beBxy2oHtSScFVc4stp~crDBZNdk5ztSxP-s-8PXuktpjL-oTJTJXIOmTm10u-UtNUpdQNZtE~CzcuaGBZE8sShWWJo2DxeilSJzklPS1rZ0h~w__&Key-Pair-Id=APKAJB334VX63D3WJ5ZQ'
// );
// const decipher = cipher.createDecipher(
//   'DES-ECB',
//   util.createBuffer(key, 'utf8')
// );

// decipher.start({ iv: util.createBuffer(iv, 'utf8') });
// decipher.update(util.createBuffer(encrypted));
// decipher.finish();

// const decryptedLink = decipher.output.getBytes();

// console.log(decryptedLink);

const countryCodes = require("./countries");
const radios = require("./done/usa/working_stations.json");

console.log(radios.length);

console.log(countryCodes["Japan"]);
