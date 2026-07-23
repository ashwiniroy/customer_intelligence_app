import {
    Paper,
    Typography,
    Chip,
    Stack,
    Divider
  } from "@mui/material";
  
  import SourceReviewCard from "./SourceReviewCard";
  
  const AIResponsePanel = () => {
    return (
      <Paper sx={{ p: 3, height: "100%" }}>
        <Typography variant="h6" mb={2}>
          AI Response
        </Typography>
  
        <Typography paragraph>
          Customers are generally satisfied with the MacBook battery
          life. Around 89% of the reviews mention excellent battery
          performance and long usage hours.
        </Typography>
  
        <Typography fontWeight={600} mb={1}>
          Overall Sentiment
        </Typography>
  
        <Chip
          label="Positive (89%)"
          color="success"
        />
  
        <Divider sx={{ my: 3 }} />
  
        <Typography fontWeight={600}>
          Key Topics
        </Typography>
  
        <Stack direction="row" spacing={1} mt={2} mb={3}>
          <Chip label="Battery" />
          <Chip label="Performance" />
          <Chip label="Charging" />
          <Chip label="Heat" />
        </Stack>
  
        <Typography fontWeight={600} mb={2}>
          Source Reviews
        </Typography>
  
        <SourceReviewCard
          customer="Ashwini Kumar"
          rating={5}
          review="Battery backup is excellent and lasts almost two days."
        />
  
        <SourceReviewCard
          customer="John Smith"
          rating={4}
          review="Performance is great but charging could be faster."
        />
      </Paper>
    );
  };
  
  export default AIResponsePanel;