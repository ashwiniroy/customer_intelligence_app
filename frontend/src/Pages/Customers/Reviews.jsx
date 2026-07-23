import { Box } from "@mui/material";

import PageHeader from "../../Components/Common/PageHeader";
import AppButton from "../../Components/Common/Button";

import ReviewToolbar from "../../Components/Reviews/ReviewToolbar";
import ReviewTable from "../../Components/Reviews/ReviewTable";

import { REVIEWS } from "../../Constants/reviews";

const Reviews = () => {
  return (
    <Box>

      <PageHeader
        title="Reviews"
        subtitle="Manage and analyze customer reviews"
        action={
          <AppButton>
            Create Review
          </AppButton>
        }
      />

      <ReviewToolbar />

      <Box
        sx={{
          height: 550,
          backgroundColor: "#fff",
          borderRadius: 2,
          p: 2,
        }}
      >
        <ReviewTable rows={REVIEWS} />
      </Box>

    </Box>
  );
};

export default Reviews;