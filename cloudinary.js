const cloudinary = require("cloudinary").v2;
const { customAlphabet } = require("nanoid");

const uniqueKeyConstants =
  "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
const uniqueKeyInitials = "tarana";
const generateUniqueID = () => {
  const id = customAlphabet(uniqueKeyConstants, 12);
  const uniqueId = `${uniqueKeyInitials}_${"thumbnail"}_${id()}`;
  return uniqueId;
};

cloudinary.config({
  cloud_name: "",
  api_key: "",
  api_secret: "",
});

function uploadToCloudinary(url, new_path = generateUniqueID()) {
  let public_id = "tarana-v2/" + new_path;
  return new Promise((resolve, reject) => {
    cloudinary.uploader.upload(
      url,
      { resource_type: "image", public_id: public_id },
      function (error, result) {
        resolve({ error: error, result: result });
      }
    );
  });
}

module.exports = uploadToCloudinary;
