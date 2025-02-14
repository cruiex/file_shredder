import React from "react";
import styled, { keyframes } from "styled-components";
import Button from "@mui/material/Button";
import CloudUploadIcon from "@mui/icons-material/CloudUpload";

const rotateGlow = keyframes`
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
`;

const StyledButtonWrapper = styled.div`
  position: relative;
  display: inline-block;

  .button-layer,
  .glow,
  .darkBorderBg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 12px;
    z-index: -1;
    overflow: hidden;
  }

  .glow {
    filter: blur(15px);
    opacity: 0.6;
    background-image: conic-gradient(
      from 180deg at 50% 50%,
      #6a1b9a,
      #8e24aa,
      #ab47bc,
      #6a1b9a
    );
    animation: ${rotateGlow} 8s linear infinite;
  }

  .darkBorderBg {
    border: 2px solid #4527a0;
    background: conic-gradient(
      from 180deg at 50% 50%,
      #1c1a33,
      #5e35b1,
      #1c1a33
    );
  }

  .whiteLayer {
    filter: blur(5px);
    background-color: rgba(255, 255, 255, 0.1);
    border: 2px solid rgba(255, 255, 255, 0.2);
  }
`;

const StyledButton = styled(Button)`
  position: relative;
  background-color: #4caf50;
  color: #fff;
  padding: 10px 20px;
  border-radius: 8px;
  overflow: hidden;

  &:hover {
    background-color: #388e3c;
  }

  .button-content {
    position: relative;
    z-index: 1;
    display: flex;
    align-items: center;
    gap: 8px;
  }
`;

const UploadButton = ({ onChange }) => (
  <StyledButtonWrapper>
    <div className="glow" />
    <div className="darkBorderBg" />
    <div className="whiteLayer" />
    <StyledButton component="label">
      <div className="button-content">
        <CloudUploadIcon />
        Upload Files
      </div>
      <input type="file" onChange={onChange} multiple hidden />
    </StyledButton>
  </StyledButtonWrapper>
);

export default UploadButton;
