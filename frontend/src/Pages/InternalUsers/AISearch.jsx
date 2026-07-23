import { Box, Grid, Typography } from "@mui/material";

import AIInputPanel from "../../Components/ai/AIInputChannel";
import SuggestedQuestions from "../../Components/ai/SuggestedQuestions";
import AIResponsePanel from "../../Components/ai/AIResponsePanel";

const AISearch = () => {
  return (
    <Box>

      <Typography
        variant="h4"
        fontWeight={700}
        mb={4}
      >
        AI Review Assistant
      </Typography>

      <Grid container spacing={3}>

        <Grid size={{ xs: 12, md: 4 }}>
          <AIInputPanel />
          <SuggestedQuestions />
        </Grid>

        <Grid size={{ xs: 12, md: 8 }}>
          <AIResponsePanel />
        </Grid>

      </Grid>

    </Box>
  );
};

export default AISearch;