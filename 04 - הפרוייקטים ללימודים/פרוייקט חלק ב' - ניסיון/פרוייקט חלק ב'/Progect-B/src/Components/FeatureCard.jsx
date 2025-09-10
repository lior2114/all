import React from 'react';
import { Paper, Typography } from '@mui/material';
import styles from './FeatureCard.module.css';

export function FeatureCard({ icon, title, description }) {
  return (
    <Paper elevation={2} className={styles.featureCard}>
      <div className={styles.featureIcon}>
        {icon}
      </div>
      <Typography variant="h5" component="h3" gutterBottom className={styles.featureTitle}>
        {title}
      </Typography>
      <Typography variant="body1" className={styles.featureDescription}>
        {description}
      </Typography>
    </Paper>
  );
}
