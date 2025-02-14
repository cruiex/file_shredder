import React, { useState } from "react";
import Button from "@mui/material/Button";
import CloudUploadIcon from "@mui/icons-material/CloudUpload";
import LockIcon from "@mui/icons-material/Lock";
import UnLockIcon from "@mui/icons-material/LockOpen";
import "./App.css";

function App() {
  const [isUploaded, setIsUploaded] = useState(false);
  const [isEncrypted, setIsEncrypted] = useState(false);
  const [isDecrypted, setIsDecrypted] = useState(false);

  const uploadFiles = async (event) => {
    const files = event.target.files;
    if (files.length > 0) {
      const formData = new FormData();
      for (let i = 0; i < files.length; i++) {
        formData.append("files", files[i]);
      }

      try {
        const response = await fetch("http://localhost:5000/upload", {
          method: "POST",
          body: formData,
        });

        if (response.ok) {
          console.log("Files uploaded successfully");
          setIsUploaded(true);
          setIsEncrypted(false); // Reset the encrypted state when new files are uploaded
          setIsDecrypted(false); // Reset decryption state
        } else {
          console.error("Upload failed");
        }
      } catch (error) {
        console.error("Error uploading files:", error);
      }
    }
  };

  const handleEncrypt = async () => {
    try {
      const response = await fetch("http://localhost:5000/encrypt", {
        method: "POST",
      });

      if (response.ok) {
        const result = await response.json();
        console.log("Files encrypted successfully:", result);

        // Make sure encrypted files are available and set the state
        setIsEncrypted(true);
        setIsDecrypted(false); // Reset decryption state

        // Optionally, handle file download or other actions here
        const encryptedFiles = result.encrypted_files;
        if (encryptedFiles && encryptedFiles.length > 0) {
          window.location.href = `http://localhost:5000/encrypted/${encryptedFiles[0]}`; // Download first encrypted file
        }
      } else {
        console.error("Encryption failed:", response.statusText);
      }
    } catch (error) {
      console.error("Error during encryption:", error);
    }
  };

  const handleDecrypt = async () => {
    try {
      const response = await fetch("http://localhost:5000/decrypt", {
        method: "POST",
      });

      if (response.ok) {
        const result = await response.json();
        console.log("Files decrypted successfully:", result);
        setIsDecrypted(true);
        setIsEncrypted(false); // Reset encryption state
      } else {
        console.error("Decryption failed:", response.statusText);
      }
    } catch (error) {
      console.error("Error during decryption:", error);
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>File Shredder using Shamir's Secret Sharing</h1>
      <Button
        variant="contained"
        component="label"
        startIcon={<CloudUploadIcon />}
        style={{ margin: "10px" }}
      >
        Upload Files
        <input type="file" onChange={uploadFiles} multiple hidden />
      </Button>

      {isUploaded && !isEncrypted && (
        <Button
          variant="contained"
          startIcon={<LockIcon />}
          onClick={handleEncrypt}
          style={{ margin: "10px", backgroundColor: "#FF5722", color: "#fff" }}
        >
          Encrypt Files
        </Button>
      )}

      {isEncrypted && (
        <Button
          variant="contained"
          startIcon={<UnLockIcon />}
          onClick={handleDecrypt}
          style={{ margin: "10px", backgroundColor: "#4CAF50", color: "#fff" }}
        >
          Decrypt Files
        </Button>
      )}

      {isDecrypted && (
        <Button
          variant="contained"
          onClick={handleShredFiles}
          style={{ margin: "10px", backgroundColor: "red", color: "white" }}
        >
          Shred Files
        </Button>
      )}
    </div>
  );
}

const handleShredFiles = async () => {
  try {
    const response = await fetch("http://localhost:5000/shred", {
      method: "POST",
    });

    if (response.ok) {
      alert("Files shredded successfully!");
      // Reset states to start fresh
      setIsUploaded(false);
      setIsEncrypted(false);
      setIsDecrypted(false);
    } else {
      console.error("Shredding failed");
    }
  } catch (error) {
    console.error("Error during shredding:", error);
  }
};

export default App;
