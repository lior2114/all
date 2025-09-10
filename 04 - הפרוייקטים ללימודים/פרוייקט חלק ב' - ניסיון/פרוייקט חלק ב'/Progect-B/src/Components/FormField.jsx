import React from 'react';
import { TextField, InputAdornment } from '@mui/material';
import styles from './FormField.module.css';

export function FormField({ 
  label, 
  name, 
  value, 
  onChange, 
  error, 
  helperText, 
  type = 'text', 
  required = false, 
  startIcon, 
  endIcon,
  className = '',
  ...props 
}) {
  return (
    <TextField
      fullWidth
      label={label}
      name={name}
      value={value}
      onChange={onChange}
      error={!!error}
      helperText={error || helperText}
      type={type}
      required={required}
      className={`${styles.formField} ${className}`}
      InputProps={{
        startAdornment: startIcon ? (
          <InputAdornment position="start">
            {startIcon}
          </InputAdornment>
        ) : undefined,
        endAdornment: endIcon ? (
          <InputAdornment position="end">
            {endIcon}
          </InputAdornment>
        ) : undefined,
      }}
      {...props}
    />
  );
}
